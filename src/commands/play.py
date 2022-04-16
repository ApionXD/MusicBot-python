import discord
import asyncio

import bot_container

from commands.command import Command
from sources import YTDLSource

song_map = {} #May need to move somewhere more central


class Play(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        guild_id = server.id
        if (guild_id in song_map):
            song_map[guild_id].append(YTDLSource.YTSource(" ".join(command_event.words[1:])))
        else:
            song_map[guild_id] = [YTDLSource.YTSource(" ".join(command_event.words[1:]))]
        if server.voice_client is None:
            await discord.utils.find(lambda m: m.id == command_event.guild_settings.voice_channel_id, server.voice_channels).connect()
        else:
            server.voice_client.disconnect()
        self.play_next_song(server, command_event.guild_settings.command_channel_id )

    # Plays next song
    def play_next_song(self, server, channel_id):
        id = server.id
        # If there is a queue
        if len(song_map[id]) > 0:
            # Sets source to be the first song in queue
            source = song_map[id][0]
            song_map[id].pop(0)
            text_channel = discord.utils.find(lambda m: m.id == channel_id, server.text_channels)
            embed = discord.Embed(title="Now Playing", url=source.data['uploader_url'])
            embed.set_image(url=source.data['thumbnails'][0]['url'])
            embed.set_author(name="MusicBot")
            embed.add_field(name="Artist", value=source.data['artist'], inline=True)
            embed.add_field(name="Track", value=source.data['track'], inline=True)
            embed.add_field(name="Duration", value=f"{int(source.data['duration'] / 60)}:{source.data['duration'] % 60}", inline=True)
            asyncio.run_coroutine_threadsafe(text_channel.send(embed=embed), bot_container.bot_instance.loop)
            server.voice_client.play(source, after=lambda x=None: self.play_next_song(server, channel_id))
        else:
            asyncio.run_coroutine_threadsafe(server.voice_client.disconnect(), bot_container.bot_instance.loop)

