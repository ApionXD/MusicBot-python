import discord

from commands.command import Command
from sources import YTDLSource

song_list = {} #May need to move somewhere more central


class Play(Command):
    perm_level = 1000
    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = discord.utils.find(lambda m: m.id == command_event.guild_settings.voice_channel_id, server.voice_channels)
        channel = server.id
        if (channel in song_list): #If play is called automatically goes to top(easier for testing not final)
            source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
            song_list[channel].insert(0, source)
        else:
            source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
            song_list[channel] = [source]

        if server.voice_client==None or not server.voice_client.is_connected(): #Sees if already in voice
            connection = await voice_channel.connect()
            await command_event.message_event.channel.send("Now Playing: "+self.check_songs(command_event, connection, server).url)
        else:
            await command_event.message_event.channel.send( #Perhaps a way to make queue share this
                "Added to queue"+" "+song_list[channel][-1].url)


    def check_songs(self, command_event, connection, server): #Keeps playing songs while there is a queue
        channel = server.id
        if song_list[channel] != [] and not server.voice_client==None and server.voice_client.is_connected():
            print(song_list[channel])
            source = song_list[channel][0]
            connection.play(source,  after= lambda x=None: command_event.message_event.channel.send(self.check_songs(command_event, connection, server)))
            song_list[channel].pop(0)
            return source
        return
