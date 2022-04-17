from commands.command import Command

class HelloWorld(Command):
    perm_level = 0

    async def run_command(self, command_event):
        await command_event.message_event.channel.send("Hello world!")
