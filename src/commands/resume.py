from commands.command import Command


class Resume(Command):
    # Permission level: Should be accessible to everyone that is able to play music
    perm_level = 1000

    async def run_command(self, command_event):
        server = command_event.message_event.guild
        # If a song is paused using the resume command will run this line resuming the song
        if server.voice_client.is_paused():
            server.voice_client.resume()
        # In the case that a song is already playing and they try to use the resume command, they will receive this message
        elif server.voice_client.is_playing():
            await command_event.message_event.channel.send("Song is currently playing, cannot resume.")
        # In the case that a song is never played and the resume command is used this message will be the output
        else:
            await command_event.message_event.channel.send("Unable to resume.")
