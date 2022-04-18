import settings
from commands.command import Command


class SetReactions(Command):
    perm_level = 5000
    async def run_command(self, command_event):
        if (len(command_event.words)==3 and not command_event.words[1]==command_event.words[2]): #Takes in two arguments to make sure command is run properly
            command_event.guild_settings.reactions = [command_event.words[1],command_event.words[2]]
            settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
            await command_event.message_event.channel.send(
                f"Bot reactions successfully changed to {command_event.guild_settings.reactions}")
        else:
            await command_event.message_event.channel.send(
                "Incorrect usage takes one good reaction one bad")
