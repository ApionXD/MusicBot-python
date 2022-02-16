import discord
import os.path
import json

import settings

command_map = {

}
settings_map = {

}


# This is a class representing the bot, it inherits from the discord.Client class
class PythonClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

    async def on_ready(self):
        print(f"Logged in as {self.user}")
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

    async def on_message(self, message):
        print(f"Recieved message in {message.channel.name}: {message.content}")
