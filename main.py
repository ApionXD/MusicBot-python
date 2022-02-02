import discord

class python_client(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")
    async def on_message(self, message):
        print(f"Recieved message in {message.channel.name}: {message.content}")

if __name__ == '__main__':
    client = python_client()
    client.run("ODI2MTI1Nzc1OTgzMjE0NjQy.YGH7lQ.oZa5hpVMJOXKxbYV760T2j4-8QY")