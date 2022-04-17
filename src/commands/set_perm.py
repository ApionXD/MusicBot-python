import settings
from commands.command import Command


class SetPerm(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000
    async def run_command(self, command_event):
        command_event.guild_settings.perm_map.get_highest_permission_level = command_event
        settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
        await command_event.message_event.channel.send(f"Permission successfully changed to {command_event.guild_settings.perm_map.get_highest_permission_level}")
