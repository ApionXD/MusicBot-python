import bot_container
import python_client

client = python_client.PythonClient()

if __name__ == '__main__':
    bot_container.bot_instance = client
    client.run("ODI2MTI1Nzc1OTgzMjE0NjQy.YGH7lQ.lukBY_bA0pTJbaeWVqxl52Y9HR0")
