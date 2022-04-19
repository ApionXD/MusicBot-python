import settings
import permission_map
from commands.command import Command


class SetPerm(Command):
    # Might need to adjust the perm level based on who we want to be able to change
    perm_level = 5000

    async def run_command(self, command_event):
        user = command_event
        #settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
        await command_event.message_event.channel.send(f"The user is {user}")

    # Basically how perms work is that you can set a user to be a specific permission level and you can set a role
    # to be a specific permission level. When a command is run, it checks what you have set, and it then gets the
    # HIGHEST number of what applies to you. So say you have role1, which is set to 100 and then your user level
    # is set to 10. Your perm level would still be 100.
    # What the set perm command needs to allow you to do is add the levels to roles and people
    # By default, the ONLY person/role assigned a perm level is the owner of the discord server
    # So they need to be able to do something like "!setperm @Admin 1000"
    # So that people with the Admin role can  run commands
    # Or "!setperm @kiarrobino 100"
    # Basically you need to figure out what role the user is talking about, then you need to get the guild settings
    # from the command event. In the guild settings, there is a permission map. That object contains a dict that
    # matches role ids to perm levels, and a dict that matches user id's to perm levels. You need to add or change
    # those dicts to change perms, and then run the save settings method to save them.
    # The "perm_level" in each command is the minimum perm level a user needs to have (maybe from their roles) to
    # run that command
    # So commands that everyone should be able to run are 0, whereas admin commands like setprefix are larger
    # Since admins should have a larger permission level

    # message_event.author
