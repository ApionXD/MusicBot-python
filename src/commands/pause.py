from commands.command import Command


class Pause(Command):
    # Permission level: Should be accessible to everyone that is able to play music
    perm_level = 1000

    async def run_command(self, command_event):
        server = command_event.message_event.guild
        # If a song is playing: execute the command to pause
        if server.voice_client.is_playing():
            server.voice_client.pause()
        # if a song is already pause: print a message to the user letting them know
        elif server.voice_client.is_paused():
            await command_event.message_event.channel.send("Song is currently paused. Use the \'Resume\' command to continue playing.")
        # If a song was never started the user will receive this message
        else:
            await command_event.message_event.channel.send("Unable to pause the song.")
