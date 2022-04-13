import asyncio

import discord
import requests
import youtube_dl

API_KEY = 'AIzaSyCTazKIZr6p04G09B6JhvobG5y_YDMHaq0'
YTDL_OPT = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


# This method takes in a search query, then queries the YouTube API for the normal link to the first video matching
# the search query
def get_top_item_link(query):
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'key': API_KEY
    }
    yt_response = requests.get("https://youtube.googleapis.com/youtube/v3/search", params=params)
    video_id = yt_response.json()["items"][0]["id"]["videoId"]
    return f"https://www.youtube.com/watch?v={video_id}"


# This class encapsulates all necessary methods for obtaining audio data from YouTube. The way it works is that the we
# query the YouTube API for the first video matching our search, then we use YTDL to get the actual link to the content
# of the video. We can feed that link into ffmpeg to transcode whatever format YT gives us into one that discord can
# process.
class YTSource(discord.FFmpegPCMAudio):
    def __init__(self, query):
        self.ytdl = youtube_dl.YoutubeDL(YTDL_OPT)
        self.url = get_top_item_link(query)
        stream_link = self.get_stream()
        super().__init__(stream_link)


    # This method uses the normal link to a YT video to fetch the data about that video, mainly
    # the actual link to the content.
    def get_stream(self):
        self.data = self.ytdl.extract_info(self.url, download=False)
        filename = self.data['url']
        return filename




