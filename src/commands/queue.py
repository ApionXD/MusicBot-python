from commands.command import Command
from commands.play import song_map
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

        await command_event.message_event.channel.send(
            "Added to queue" +" " + song_map[server.id][-1].url)

