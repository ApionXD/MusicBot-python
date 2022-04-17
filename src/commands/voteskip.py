import asyncio
from distutils.command import check

import discord

import bot_container
import settings
import commands.play
import commands.skip
from commands.command import Command

messagess_check = list() #list to store messgaes to ensure one vote for
vote_reactions = {} #holds users and what their vote was

class VoteSkip(Command):
    perm_level = 0

    def check(reaction, user):
        return True

    async def run_command(self, command_event):
        server = command_event.message_event.guild
        voice_channel = server.voice_client
        global messagess_check
        if (not server.voice_client==None and voice_channel.is_connected() and voice_channel.is_playing()):
            embed = commands.play.embed
            embed.title = "Now voting to skip"
            msg = await command_event.message_event.channel.send(embed=
                embed)
            messagess_check.append(msg.id)

            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
            await asyncio.sleep(10)

            numSkip = 0
            numNonSkip = 0
            potential = [vote_reactions[key] for key in vote_reactions if key.endswith(str(msg.id))]

            for i in potential:
                if '👍' in i:
                    numNonSkip+=1
                else:
                    numSkip+=1
                #del vote_reactions[i.key] #TODO delete all potentials after stored
            member_getter = discord.utils.get(server.channels, id=command_event.guild_settings.voice_channel_id) #TODO Fix error where doesn't register people joined before bot/still playing same song
            members = member_getter.members
            numListening = 0
            for member in members:
                numListening += 1

            #print(potential, numNonSkip, numSkip, numListening, members)
            messagess_check.remove(msg.id)
            if (numSkip*2>=numListening):# majority rules voting
                await command_event.message_event.channel.send(
                    ("Skip!"))
                if command_event.message_event.guild.voice_client is not None: #Can maybe be combined with skip
                    command_event.message_event.guild.voice_client.stop()
            else:
                await command_event.message_event.channel.send(
                    ("Voting Has Ended. The song stays."))

        else:
            await command_event.message_event.channel.send(
                ("You aren't connected to a server"))

