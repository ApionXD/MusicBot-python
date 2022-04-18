import asyncio
from distutils.command import check

import discord

import bot_container
import settings
import commands.play
import commands.skip
from commands.command import Command
from commands.play import song_map
from sources import YTDLSource

messagess_check = list() #list to store messgaes to ensure one vote for
vote_reactions = {} #holds users and what their vote was

class VoteSkip(Command):
    perm_level = 0

    def check(reaction, user):
        return True

    async def start_vote_cur(self, command_event, embed, location=-1): #manages the whole voting system
        global messagess_check
        server = command_event.message_event.guild
        voice_channel = server.voice_client
        msg = await command_event.message_event.channel.send(embed= #sends out now voting message
                                                             embed)

        messagess_check.append(msg.id) #adds msg to messages that emotes need to be managed on
        reactions = command_event.guild_settings.reactions #gets guilds prefereed messages
        good_reaction = reactions[0] if len(reactions) > 0 else "👍" #default reaction if can't read in
        bad_reaction = reactions[1] if len(reactions) > 1 else "👎"

        await msg.add_reaction(good_reaction)
        await msg.add_reaction(bad_reaction)
        await asyncio.sleep(command_event.guild_settings.timer_reactions) #sleeps for desired time before getting resutls

        numSkip = 0
        numNonSkip = 0
        potential = [key for key in vote_reactions if key.endswith(str(msg.id))]

        for i in potential:
            if good_reaction in vote_reactions[i]:
                numNonSkip += 1
            else:
                numSkip += 1

        for key in potential: del vote_reactions[key] #deletes all potential to free up space

        member_getter = discord.utils.get(server.channels, id=command_event.guild_settings.voice_channel_id) #used to get members in desired voice
        members = member_getter.voice_states.keys()
        numListening = -1 #starts at -1 to remove the bot
        for member in members:
            numListening += 1

        #print(potential, numNonSkip, numSkip, numListening, members)
        messagess_check.remove(msg.id) #removes messages so the vote is no longer monitored

        if (voice_channel.is_playing() and embed.url == commands.play.embed.url): #sees if the same song is still playing if ran default or with current song
            if (numSkip * 2 >= numListening):  # majority rules voting
                if command_event.message_event.guild.voice_client is not None:  # Can maybe be combined with skip
                    embed.title = "Now Skipping"
                    await command_event.message_event.channel.send(embed=
                                                                   embed)
                    command_event.message_event.guild.voice_client.stop()
            else:
                embed.title = "Voting has ended. The song stays"
                await command_event.message_event.channel.send(embed=
                                                               embed)
        elif not location==-1 and voice_channel.is_playing(): #sees if soong in queue is the one that needs to be changed location used to know what to use
            if (numSkip * 2 >= numListening):  # majority rules voting
                location = -1
                for i in range(len(song_map[server.id])): #looks for location to make sure queue didn't change in the time period
                    if (song_map[server.id][i].data['uploader_url'] == embed.url):
                        location = i
                if not location==-1:
                    song_map[server.id].pop(location)
                    embed.title = "Now removing from queue"
                    await command_event.message_event.channel.send(embed=
                                                                   embed)
            else:
                embed.title = "Voting has ended. The song stays"
                await command_event.message_event.channel.send(embed=
                                                               embed)
        else:
            embed.title = "The song ended already."
            await command_event.message_event.channel.send(embed=
                                                             embed)

    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = server.voice_client
        if (len(command_event.words)>1): #makes a source since YTDL doesn't always find exact names
            source = YTDLSource.YTSource(" ".join(command_event.words[1:]))
        embed = commands.play.embed
        if (len(command_event.words)==1 or len(command_event.words)>1 and embed.url==source.data['uploader_url']) and not server.voice_client is None and voice_channel.is_connected() and voice_channel.is_playing():
            #sees if the one playing was chosen
            embed.title = "Now voting to skip"
            await self.start_vote_cur(command_event, embed)
        elif len(command_event.words)>1 and not server.voice_client == None and voice_channel.is_connected() and voice_channel.is_playing():

            location = -1
            for i in range(len(song_map[server.id])): #tries to find source
                if (song_map[server.id][i].url == source.url):
                    location = i

            if not location==-1: #makes embed and runs start_vote_cur if found
                embed = discord.Embed(title="Now voting to skip", url=source.data['uploader_url'])
                embed.set_image(url=source.data['thumbnails'][0]['url'])
                embed.set_author(name="Beedle")
                embed.set_footer(text="A reaction driven music bot!")
                if 'artist' in source.data:
                    embed.add_field(name="Artist", value=source.data['artist'], inline=True)
                if 'track' in source.data:
                    embed.add_field(name="Track", value=source.data['track'], inline=True)
                else:
                    embed.add_field(name="Title", value=source.data['title'])
                if 'duration' in source.data:
                    duration_str = f"{int(source.data['duration'] / 60)}:"
                    if duration_str == "0:":
                        duration_str = ':'
                    seconds = source.data['duration'] % 60
                    if seconds < 10:
                        duration_str += f"0{seconds}"
                    else:
                        duration_str += f"{seconds}"
                    embed.add_field(name="Duration", value=duration_str, inline=True)
                await self.start_vote_cur(command_event, embed, location)
            else:
                await command_event.message_event.channel.send(
                    "Can't find that song in queue")



        else:
            await command_event.message_event.channel.send(
                "No song is currently playing")

