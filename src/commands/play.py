import discord

import commands.command
import sources.YTDLSource
from sources import YTDLSource


class Play(commands.command.Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = server.voice_channels[0]
        connection = await voice_channel.connect()
        source = sources.YTDLSource.YTSource(" ".join(command_event.words[1:]))
        connection.play(source)



