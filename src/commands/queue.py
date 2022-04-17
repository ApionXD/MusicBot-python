import discord

from commands.command import Command
from commands.play import song_map, play_next_song
from sources import YTDLSource


class Queue(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        #voice_channel = [x for x in server.voice_channels if x.id == command_event.guild_settings.voice_channel_id][0]
        source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
        if server.id in song_map:
            song_map[server.id].append(source)
        else:
            song_map[server.id] = [source]
            play_next_song(server, command_event.guild_settings.command_channel_id, command_event.guild_settings.voice_channel_id)
        embed = discord.Embed(title="Added to queue", url=source.data['uploader_url'])
        embed.set_image(url=source.data['thumbnails'][0]['url'])
        embed.set_author(name="MusicBot")
        if 'artist' in source.data:
            embed.add_field(name="Artist", value=source.data['artist'], inline=True)
        if 'track' in source.data:
            embed.add_field(name="Track", value=source.data['track'], inline=True)
        if 'duration' in source.data:
            embed.add_field(name="Duration",
                            value=f"{int(source.data['duration'] / 60)}:{source.data['duration'] % 60}",
                            inline=True)
        await command_event.message_event.channel.send(embed=embed)

