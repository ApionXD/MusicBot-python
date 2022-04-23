import settings
import discord
import permission_map
from commands.command import Command


class SetPermu(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000

    async def run_command(self, command_event):
        # Stores the second string command_event
        if len(command_event.words)==3:
            user = command_event.words[1]
            username = command_event.words[1]
            # Stores the third string in command_event (Should be in the form of an int)
            permission_level = command_event.words[2]
            user = user.replace("@", "")
            user = user.replace("<", "")
            user = user.replace(">", "")
            members = command_event.message_event.guild.fetch_members()
            id = None
            async for member in members:
                if member.name==user:
                    print("found")
                    id = str(member.id)

            if (id is not None):
                command_event.guild_settings.perm_map.user_map[id] = int(permission_level)
                settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
                await command_event.message_event.channel.send(
                    f"Updated {username} to {command_event.guild_settings.perm_map.user_map[id]}")
            else:
                await command_event.message_event.channel.send(
                    f"Couldn't find user")
        else:
            await command_event.message_event.channel.send(
                f"Incorrect usage. Takes 2 arguments")

