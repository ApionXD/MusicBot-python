import os

from discord import Intents
from dotenv import load_dotenv

import bot_container
import python_client

client = python_client.PythonClient(intents=Intents.all())

if __name__ == '__main__':
    load_dotenv()
    bot_container.bot_instance = client
    client.run(os.getenv("TOKEN"))
