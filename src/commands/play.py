import concurrent

import discord
import asyncio

import bot_container

from commands.command import Command
from sources import YTDLSource
# May need to move somewhere more central
song_map = {}


# Plays next song
# This entire method is slightly sketchy. The main issue is that the coroutine that the play method accepts can't be async
# This means that we have to use the main bot event loop to run ANY ASYNC METHODS. That's what the asyncio methods do.
# I hate this.
def play_next_song(server, command_channel_id, voice_channel_id):
    id = server.id
    # If there is a queue
    if len(song_map[id]) > 0:
        # Joins voice channel and reruns this command
        if server.voice_client is None:
            voice_channel = discord.utils.find(lambda m: m.id == voice_channel_id, server.voice_channels)
            future = asyncio.run_coroutine_threadsafe(voice_channel.connect(), bot_container.bot_instance.loop)
            # Uhhhhhh slightly sketchy. For some reason i couldn't get the current thread to block until the above future finished
            # But I CAN add a callback? Weird and annoying, but should work.
            future.add_done_callback(lambda y: play_next_song(server, command_channel_id, voice_channel_id))
            return
        # Sets source to be the first song in queue
        source = song_map[id][0]
        song_map[id].pop(0)
        text_channel = discord.utils.find(lambda m: m.id == command_channel_id, server.text_channels)
        embed = discord.Embed(title="Now Playing", url=source.data['uploader_url'])
        embed.set_image(url=source.data['thumbnails'][0]['url'])
        embed.set_author(name="Beedle")
        embed.set_footer(text="A reaction driven music bot!")
        if 'artist' in source.data:
            embed.add_field(name="Artist", value=source.data['artist'], inline=True)
        if 'track' in source.data:
            embed.add_field(name="Track", value=source.data['track'], inline=True)
        else:
            embed.add_field(name="Title", value=source.data['title'])
        if 'duration' in source.data:
            duration_str = f"{int(source.data['duration'] / 60)}:"
            if duration_str == "0:":
                duration_str = ':'
            seconds = source.data['duration'] % 60
            if seconds < 10:
                duration_str += f"0{seconds}"
            else:
                duration_str += f"{seconds}"
            embed.add_field(name="Duration", value=duration_str,
                            inline=True)
        asyncio.run_coroutine_threadsafe(text_channel.send(embed=embed), bot_container.bot_instance.loop)
        server.voice_client.play(source, after=lambda x=None: play_next_song(server, command_channel_id, voice_channel_id))
    else:
        asyncio.run_coroutine_threadsafe(server.voice_client.disconnect(), bot_container.bot_instance.loop)


class Play(Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        guild_id = server.id
        if (guild_id in song_map):
            song_map[guild_id] = [(YTDLSource.YTSource(" ".join(command_event.words[1:])))] + song_map[guild_id][1:]
        else:
            song_map[guild_id] = [YTDLSource.YTSource(" ".join(command_event.words[1:]))]
        if server.voice_client is None:
            play_next_song(server, command_event.guild_settings.command_channel_id,
                           command_event.guild_settings.voice_channel_id)

