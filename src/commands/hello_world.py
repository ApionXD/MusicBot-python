from commands.command import Command


class HelloWorld(Command):
    perm_level = 0

    async def run_command(self, command_event):
        user = command_event.message_event.author
        await command_event.message_event.channel.send(f"Hello {user}!")
