Beedle is a Discord music bot!

### Features:

- Reaction based voting
- Supports multiple sources (YouTube, Soundcloud)
- Embedded responses that look great
- Customizable permissions
- Persistent server-specific settings
  <br>

### Instructions:
- Bot Setup:
  Visit the [Discord Developer Portal](https://discord.com/developers/applications) \
  Create a new Application and name it \
  In the settings menu, go to 'Bot' \
  Click 'Add Bot' \
  Adjust desired settings. You may fine tune the permissions if you'd like, but it is easiest to make the bot an Administrator \
  Check 'Message Content Intent' (REQUIRED) \
  Click 'Reset Token' \
  Note down the generated token \
  Navigate to the 'OAuth2' menu on the left \
  Navigate to 'URL Generator' and click 'bot' under the scopes section \ 
  Select permissions (Administrator) \
  Paste the generated link into your browser, and choose the server you would like to add Beedle to
  

- Docker:\
  Download, then run `docker build --tag [image_name] .`
- Put your bot token in the TOKEN environment variable
- Linux:\
  Ensure you have the dependencies listed below installed and on your $PATH variable, then run `pip3 install -r requirements.txt`, then run `python3 main.py`
  Either make a .env file containing your bot token, or put your token in the TOKEN environment variable\
- Windows:\
  You will need to download ffmpeg binaries from [here](https://github.com/BtbN/FFmpeg-Builds/releases) \
  Place them somewhere on your path (Google if you don't know what this means)
  Make sure you have Python 3 installed, then double click main.py
  Alternatively, you can open a command prompt and run `python main.py` or `py main.py`\
  <br>
  When the bot is added to a new guild, by default only the server owner will have permissions to run commands. They must assign permissions to roles or users by using the !setpermu or !setpermr commands

### Command List:

Note: The brackets in the command signify a mandatory parameter. The brackets following the description of the commands signify the permission level required to run the command.\
<br>
!getperms - Prints the permission level of the person running the command [0]\
!leave - Disconnects Beedle from its current voice channel [1000]\
!play [query] - Adds the first YouTube result for query to the front of the queue [1000]\
!queue [query] - Adds the first YouTube search result for query to the back of the queue [500]\
!setprefix [prefix] - Sets the prefix to invoke the bot to prefix (default !) [5000]\
!skip - Skips the song currently playing [1000]\
!help - Prints the help manual [0]\
!pause - Stops the current song playing [1000]\
!resume - Begins playing song from where it was paused [1000]\
!setpermu [User] [permLevel] - Changes the permission level of the specified user [5000]\
!setpermr [Role] [permLevel] - Changes the permission level of the specified role [5000]\
!soundcloud [query] - The play command, but for Soundcloud instead of YouTube [1000] \
!voteskip <songName> - Sets up a vote for skipping the given song, or the song currently playing if no song is given \
!setreactions [dontSkipReaction] [skipReactions] - Sets the reactions for !voteskip \
!votetimer [time] - Sets the amount of time the !voteskip command listens fotr reactions \
!showqueue - Shows the songs currently queued

<br>
Dependencies: \

- Python 3
- ffmpeg
- libopus
### Problem:
Most existing Discord bots don't really offer ways to allow users to vote on what is being played. This problem is what
we believe our bot does better than most, as we have a system that allows for users to vote on what is queued. The voting is also 
done by reactions, which we think is much more intuitive than other bots, which use commands to vote to skip songs.
We also have a permissions based system that allows server administrators to play what they would like, regardless of what others
want. These are not all of the features of our bot, but we believe this is what sets it apart from other music bots.

### Division Of Work:
  #### Mason: I did most of the base structure of the bot, including the permission system and the command structure as well as implementing the sources. I also implemented the structure for settings, and created the Dockerfile
  #### Kunle: Created almost everything related to the playlist system, including the queue command, parts of the play command, the skip command, and the showqueue command. Also implemented almost everything to do with reaction based voting.
  #### Kyle: The resume/pause command, the help command, a large chunk of the README, and parts of the setperm commands \ 
These are rough descriptions, everyone kind of worked on everything. 

### Notes:
When beginning this project, we anticipated much more difficulty in getting music data in a format that Discord can process. 
This turned out to be quite easy, and it drastically lowered the complexity of the bot 
