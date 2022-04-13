import discord
import os.path
import settings
import commands.play
import commands.hello_world
import commands.command_event

# This is a class representing the bot, it inherits from the discord.Client class
class PythonClient(discord.Client):
    def __init__(self):
        self.command_map = dict()
        self.settings_map = dict()
        discord.Client.__init__(self)
        # Register commands here
        self.command_map["hello"] = commands.hello_world.HelloWorld()
        self.command_map["play"] = commands.play.Play()

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        # Loop through all guilds and generate settings
        # Eventually we want to deserialize/reserialize settings objects to/from JSON
        # We also want to add stuff like roles/perms to settings objects
        for g in self.guilds:
            settings_file_name = f"settings/{g.id}.json"
            if os.path.exists(settings_file_name):
                None
            else:
                print(f"Settings file for {g.name} not found! Creating one now")
                guild_settings = settings.Settings()
                if not os.path.exists("settings/"):
                    os.mkdir("settings")
                settings_file = open(settings_file_name, 'w')
                settings_file.write(str(guild_settings))
                settings_file.close()

    async def on_message(self, message_event):
        # Checks to see if the message is a bot command
        # This will need to check the guild settings for the prefix, right now it only looks to see if the
        # message starts with '!"
        # Also need to add exceptions for when a message references a command that isn't registered
        if message_event.content[0] == '!':
            words = message_event.content[1:].split()
            # The first word of the message, which should be the name of the command
            command_name = words[0]
            # The CommandEvent object, which stores stuff relevant to the CURRENT call of the command
            # Should probably add words to this object
            command_event = commands.command_event.CommandEvent(message_event)
            # Gets the previously registered command by name
            command = self.command_map[command_name]
            # Runs the command
            await command.run_command(command_event)

