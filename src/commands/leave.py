import discord

import settings
from commands.command import Command
#from commands.play import video_list


class Leave(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = server.voice_client
        if (not server.voice_client==None and voice_channel.is_connected()):
            await voice_channel.disconnect()
        else:
            await command_event.message_event.channel.send(
                ("You aren't connected to a server"))
      #  if (len(video_list)>0):
      #      video_list.pop(0)



