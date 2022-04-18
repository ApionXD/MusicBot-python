import settings
from commands.command import Command


class SetTimer(Command):
    perm_level = 5000
    async def run_command(self, command_event):
        if (len(command_event.words)==2 and command_event.words[1].isdigit()): #only accepts one argument might need to ensure proper use
            command_event.guild_settings.timer_reactions = int(command_event.words[1])
            settings.save_settings(command_event.message_event.guild.id, command_event.message_event.guild.name)
            await command_event.message_event.channel.send(
                f"Bot reactions timer successfully changed to {command_event.guild_settings.timer_reactions} seconds")
        else:
            await command_event.message_event.channel.send(
                "Incorrect usage takes one number")
