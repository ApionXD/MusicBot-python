from commands.command import Command


class Help(Command):
    perm_level = 0

    async def run_command(self, command_event):
        await command_event.message_event.channel.send(
            "--------------- Discord Music Bot Manual ---------------\n"
            "To command the bot to perform an action requires the command prefix to be present prior to the command.\n"
            "The default command prefix for this bot is \'!\'\n"
            "To change the default prefix for this bot, use the command SetPrefix (For SetPrefix use information "
            "please visit the commands section).\n"
            "This bot offers a wide range of commands to perform all your music playing needs.\n"
            "COMMANDS\n"
            "\t- HelloWorld : ((PREFIX)HelloWorld) -> Simple command that simply has the bot say \'Hello\' to users.\n"
            "\t- SetPrefix : ((PREFIX)SetPrefix PREFIX) -> This command changes the prefix to enter a command. Once "
            "changed, to enter a command users must first enter the new prefix followed by their desired command.\n"
            "\t- Play : ((PREFIX)Play URL) -> This command has the bot join a server voice channel and play the user's "
            "requested song via a URL to the song on Youtube.\n"
            "\t- Queue : ((PREFIX)Queue URL) -> This command takes the song specified by the user from the URL provided "
            "and appends it to a list. When the current song playing finishes, the first song in the queue will play.\n"
            "\t- Skip : ((PREFIX)Skip) -> This command terminates the current song playing. If there is another song in "
            "the queue it will begin playing, if not the bot will idle until the next command.\n"
            "\t- Vote : ((PREFIX)Vote) -> Lets users vote to skip the song that is currently playing. If the majority "
            "of people in the channel vote, the song that is currently playing is terminated and the next song in the "
            "queue begins playing. If there is no other songs in the queue, the bot plays nothing and waits for its "
            "next command. (SUBJECT TO CHANGE)\n"
            "\t- Leave : ((PREFIX)Leave) -> This command removes the bot from its the current voice channel, stopping "
            "it from playing.\n"
            "\t- GetPerm : ((PREFIX)GetPerm) -> This command returns the permission level... not sure of what.\n"
            "\t- Help : ((PREFIX)Help) -> Displays the manual.\n"
            )
