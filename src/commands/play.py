import discord

from commands.command import Command
from sources import YTDLSource


class Play(Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = [x for x in server.voice_channels if x.id == command_event.guild_settings.voice_channel_id][0]
        connection = await voice_channel.connect()
        source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
        connection.play(source)



