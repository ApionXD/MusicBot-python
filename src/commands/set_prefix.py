import settings
from commands.command import Command


class SetPrefix(Command):
    async def run_command(self, command_event):
        command_event.guild_settings.prefix = command_event.words[1]
        settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
        await command_event.message_event.channel.send(f"Bot prefix successfully changed to {command_event.guild_settings.prefix}")
