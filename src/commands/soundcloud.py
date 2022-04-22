from commands.play import song_map, play_next_song
from commands.command import Command
from sources import YTDLSource


class Soundcloud(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        guild_id = server.id
        if (guild_id in song_map):
            song_map[guild_id] = [(YTDLSource(" ".join(command_event.words[1:])))] + song_map[guild_id][1:]
        else:
            song_map[guild_id] = [YTDLSource.SoundcloudSource(" ".join(command_event.words[1:]))]
        if server.voice_client is None:
            play_next_song(server, command_event.guild_settings.command_channel_id,
                           command_event.guild_settings.voice_channel_id)
