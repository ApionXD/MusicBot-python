import settings
import permission_map
from commands.command import Command


class SetPerm(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000

    async def run_command(self, command_event):
        # Stores the second string command_event
        user = command_event.words[1]
        # Stores the third string in command_event (Should be in the form of an int)
        permission_level = command_event.words[2]
        # Store user id (Don't think I will need this but for the time being)
        user_id = command_event.message_event.author

        command_event.guild_settings.perm_map.role_map[user] = permission_level
        command_event.guild_settings.perm_map.user_map.update(user=permission_level)
        settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
        await command_event.message_event.channel.send(f"Updated {user} to {command_event.guild_settings.perm_map.role_map[user]}")

