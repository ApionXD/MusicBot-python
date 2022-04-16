import json

import discord
import os.path
import settings
import command_map
from commands import command_event

# This is a class representing the bot, it inherits from the discord.Client class
class PythonClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)
        self.command_map = command_map.command_map
        self.settings_map = settings.settings_map


    async def on_ready(self):
        print(f"Logged in as {self.user}")
        settings.load_settings(self.guilds)


    async def on_message(self, message_event):
        if not message_event.author.bot:
            settings = self.settings_map[message_event.guild.id]
            prefix = settings.prefix
            command_channel_id = settings.command_channel_id
            # Checks to see if the message is a bot command
            # This will need to check the guild settings for the prefix
            # Also need to add exceptions for when a message references a command that isn't registered
            if message_event.channel.id == command_channel_id and message_event.content[0] == prefix:
                words = message_event.content[1:].split()
                # The first word of the message, which should be the name of the command
                command_name = words[0]
                # The CommandEvent object, which stores stuff relevant to the CURRENT call of the command
                # Should probably add words to this object
                new_command_event = command_event.CommandEvent(message_event, self.settings_map[message_event.guild.id])
                if not command_name in self.command_map:
                    await message_event.channel.send_message("Command not found!")
                    return
                # Gets the previously registered command by name
                command = self.command_map[command_name]
                # Runs the command
                if settings.perm_map.get_highest_permission_level(message_event.author) >= command.perm_level:
                    await command.run_command(new_command_event)
                else:
                    await message_event.channel.send("You don't have permission to run this command! "
                                                     "You have permission level "
                                                     f"{settings.perm_map.get_highest_permission_level(message_event.author)}"
                                                     f" but the command requires {command.perm_level}")

