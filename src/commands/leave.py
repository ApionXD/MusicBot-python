import discord

import settings
from commands.command import Command
#from commands.play import video_list


class Leave(Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = server.voice_client
        connection = await voice_channel.disconnect()
      #  if (len(video_list)>0):
      #      video_list.pop(0)



