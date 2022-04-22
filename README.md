Beedle is a Discord music bot!

### Features:

- Reaction based voting
- Supports multiple sources
- Customizable permissions
- Server-specific settings
  <br>

### Instructions:

- Docker:\
  Download, then run `docker build --tag [image_name] .`
- Linux:\
  Ensure you have the dependencies listed below installed and on your $PATH variable, then run `pip3 install -r requirements.txt`, then run `python3 main.py`
- Windows:\
  You will need to download ffmpeg binaries from [here](https://github.com/BtbN/FFmpeg-Builds/releases) \
  Place them somewhere on your path (Google if you don't know what this means)
  Make sure you have Python 3 installed, then double click main.py
  Alternatively, you can open a command prompt and run `python main.py` or `py main.py`\
  <br>
  When the bot is added to a new guild, by default only the server owner will have permissions to run commands. They must assign permissions to roles or users by using the [INSERT ROLE COMMANDS HERE] commands

### Command List:

Note: The brackets in the command signify a mandatory parameter. The brackets following the description of the commands signify the permission level required to run the command.\
<br>
!getperms - Prints the permission level of the person running the command [0]\
!leave - Disconnects Beedle from its current voice channel [1000]\
!play [query] - Adds the first YouTube result for query to the front of the queue [1000]\
!queue [query] - Adds the first YouTube search result for query to the back of the queue [500]\
!setprefix [prefix] - Sets the prefix to invoke the bot to prefix (default !) [5000]\
!skip - Skips the song currently playing [1000]\
<br>
Dependencies: \

- Python 3
- ffmpeg
- libopus
