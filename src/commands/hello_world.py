from commands.command import Command


class HelloWorld(Command):
    def __init__(self):
        None

    async def run_command(self, command_event):
        await command_event.message_event.channel.send("Hello world!")
