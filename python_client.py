import discord


# This is a class representing the bot, it inherits from the discord.Client class
class PythonClient(discord.Client):
    def __init__(self):
        discord.Client.__init__(self)

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        print(f"Recieved message in {message.channel.name}: {message.content}")
