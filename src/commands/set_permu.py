import settings
import discord
import permission_map
from commands.command import Command


class SetPermu(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000

    async def run_command(self, command_event):
        # Stores the second string command_event
        user = command_event.words[1]
        username = command_event.words[1]
        # Stores the third string in command_event (Should be in the form of an int)
        permission_level = command_event.words[2]
        user = user.replace("@", "")
        user = user.replace("<", "")
        user = user.replace(">", "")

        command_event.guild_settings.perm_map.user_map[user] = int(permission_level)
        settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
        await command_event.message_event.channel.send(f"Updated {username} to {command_event.guild_settings.perm_map.user_map[user]}")

