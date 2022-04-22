import discord

from commands.command import Command
from commands.play import song_map

class ShowQueue(Command):
    perm_level = 0
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        if (server.id in song_map and len(song_map[server.id])>0): #sees if there is anything in queue
            for i in range(len(song_map[server.id])): #loops through songs then prints them out
                source = song_map[server.id][i]
                embed = discord.Embed(title=i+1, url=source.data['uploader_url']) #uploader_url because that is how it is stored in embed
                embed.set_image(url=source.data['thumbnails'][0]['url'])
                embed.set_author(name="MusicBot")
                if 'artist' in source.data:
                    embed.add_field(name="Artist", value=source.data['artist'], inline=True)
                if 'track' in source.data:
                    embed.add_field(name="Track", value=source.data['track'], inline=True)
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
                await command_event.message_event.channel.send(embed=embed)
        else:
            await command_event.message_event.channel.send("No messages in queue")