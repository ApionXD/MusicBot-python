import commands.command
from commands import command


class HelloWorld(command.Command):
    def __init__(self):
        None

    async def run_command(self, command_event):
        await command_event.message_event.channel.send("Hello world!")
