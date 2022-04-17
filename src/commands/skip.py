from commands.command import Command
from commands.play import song_map, play_next_song


class Skip(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        if command_event.message_event.guild.voice_client is not None:
                command_event.message_event.guild.voice_client.stop()
                        
