import discord

from commands.command import Command
from sources import YTDLSource

song_list = {} #May need to move somewhere more central


class Play(Command):
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = [x for x in server.voice_channels if x.id == command_event.guild_settings.voice_channel_id][0]
        channel = server.id
        if (channel in song_list): #If play is called automatically goes to top(easier for testing not final)
            song_list[channel].insert(0, command_event.words[1:])
        else:
            song_list[channel] = command_event.words[1:]

        if server.voice_client==None or not server.voice_client.is_connected(): #Sees if already in voice
            connection = await voice_channel.connect()
            self.check_songs(command_event, connection, server)
        else:
            await command_event.message_event.channel.send( #Perhaps a way to make queue share this
                "Added to queue")


    def check_songs(self, command_event, connection, server): #Keeps playing songs while there is a queue
        channel = server.id
        if song_list[channel] != [] and not server.voice_client==None and server.voice_client.is_connected():
            source = YTDLSource.YTSource(" ".join(song_list[channel][0]))
            song_list[channel].pop(0)
            connection.play(source, after=lambda x=None: self.check_songs(command_event, connection, server))
