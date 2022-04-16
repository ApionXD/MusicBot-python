from commands import command
class GetPerm(command.Command):
    async def run_command(self, command_event):
        await command_event.message_event.channel.send(command_event.guild_settings.perm_map.get_highest_permission_level(command_event.message_event.author))