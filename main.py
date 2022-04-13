'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Libraries needed:
        - discord
        - youtube-dl
        - pynacl (If it does not download automatically with discord)
        - ffmpeg (Needs to be installed on machine, not imported)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import os
import discord
import youtube_dl
from discord.ext import commands

# Variable storing the token to access the bot in my server (DO NOT CHANGE/ ERASE)
TOKEN = 'OTYwOTgyOTkyOTMzNzQ4Nzk2.YkyXJw.Gnd9CbO1ZiuHu7R5_sGb0VAcexA'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print("The bot is ready!")


# Bot Function - HELLO - Definition
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")


# Bot Function - PLAY - Definition
@bot.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current song to end or use the 'stop' command.")
        return
    # Makes the Bot join the voice channel named 'Test'
    voice_channel = discord.utils.get(ctx.guild.voice_channels, name='Test')
    await voice_channel.connect()
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    ydl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_options) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


# Bot Function - LEAVE - Definition
@bot.command()
async def leave(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("ERROR: Bot is not connected to a voice channel.")


# Bot Function - PAUSE - Definition
@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("ERROR: Bot is not currently playing anything.")


# Bot Function - RESUME - Definition
@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("ERROR: Bot is currently playing.")


# Bot Function - STOP - Definition
@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()


bot.run(TOKEN)
