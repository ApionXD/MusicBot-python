from commands.command import Command
from commands.play import song_list, Play
from sources import YTDLSource


class Queue(Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = [x for x in server.voice_channels if x.id == command_event.guild_settings.voice_channel_id][0]
        if (len(command_event.words)>1):
            if len(song_list[server.id])==0 and (
                    server.voice_client is None or (server.voice_client is not None and not server.voice_client.is_playing())):
                Play.run_command(command_event)
            else:
                source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
                song_list[server.id].append(source)
                await command_event.message_event.channel.send(
                "Added to queue"+" "+song_list[server.id][-1].url)
        else:
            if len(song_list[server.id])>0:
                await command_event.message_event.channel.send(
                    ("Printing out the current queue"))
                for i in range(len(song_list[server.id])):
                    await command_event.message_event.channel.send(
                        (str(i+1)+": "+song_list[server.id][i].url))
            else:
                await command_event.message_event.channel.send(
                    ("The queue is empty"))