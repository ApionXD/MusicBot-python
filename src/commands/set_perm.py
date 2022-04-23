import settings
import permission_map
from commands.command import Command


class SetPerm(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000

    async def run_command(self, command_event):
        if len(command_event.words) == 3:
            role = command_event.words[1]
            rolename = command_event.words[1]
            # Stores the third string in command_event (Should be in the form of an int)
            permission_level = command_event.words[2]
            role = role.replace("@", "")
            role = role.replace("<", "")
            role = role.replace(">", "")
            roles = await command_event.message_event.guild.fetch_roles()
            id = None
            for r in roles:
                if r.name == role:
                    print("found")
                    id = str(r.id)

            if (id is not None):
                command_event.guild_settings.perm_map.role_map[id] = int(permission_level)
                settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
                await command_event.message_event.channel.send(
                    f"Updated {rolename} to {command_event.guild_settings.perm_map.role_map[id]}")
            else:
                await command_event.message_event.channel.send(
                    f"Couldn't find role")
        else:
            await command_event.message_event.channel.send(
                f"Incorrect usage. Takes 2 arguments")

