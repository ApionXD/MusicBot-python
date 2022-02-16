import discord
import os.path
import commands.command_event
import commands.hello_world

import settings

command_map = {

}
settings_map = {

}


# This is a class representing the bot, it inherits from the discord.Client class
class PythonClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)
        command_map["hello"] = commands.hello_world.HelloWorld()

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
        if message.content[0] == '!':
            words = message.content[1:].split()
            command_name = words[0]
            print(f"Command recieved in {message.channel.name}: {command_name}")
            command_event = commands.command_event.CommandEvent(message)
            command = command_map[command_name]
            await command.run_command(command_event)

