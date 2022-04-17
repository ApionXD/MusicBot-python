from commands.command import Command


class Help(Command):
    perm_level = 0

    async def run_command(self, command_event):
        await command_event.message_event.channel.send(
            "-------------------------------- Discord Music Bot Manual ---------------------------------\n\n"
            "\t-\t HelloWorld [PL=0] : ((PREFIX)HelloWorld) -> Simple command that simply has the bot say \'Hello\' to users.\n\n"
            "\t-\t SetPrefix [PL=5000] : ((PREFIX)SetPrefix PREFIX) -> This command changes the prefix to enter a command. Once "
            "changed, to enter a command users must first enter the new prefix followed by their desired command.\n\n"
            "\t-\t Play [PL=1000] : ((PREFIX)Play URL) -> This command has the bot join a server voice channel and play the user's "
            "requested song via a URL to the song on Youtube.\n\n"
            "\t-\t Queue [PL=1000] : ((PREFIX)Queue URL) -> This command takes the song specified by the user from the URL provided "
            "and appends it to a list. When the current song playing finishes, the first song in the queue will play.\n\n"
            "\t-\t Skip [PL=] : ((PREFIX)Skip) -> This command terminates the current song playing. If there is another song in "
            "the queue it will begin playing, if not the bot will idle until the next command.\n\n"
            "\t-\t Leave [PL=1000] : ((PREFIX)Leave) -> This command removes the bot from its the current voice channel, stopping "
            "it from playing.\n\n"
            "\t-\t GetPerm [PL=0] : ((PREFIX)GetPerm) -> This command returns the permission level (PL). Permission levels vary based"
            "on the role in the server and can be assigned to both users and the bot. Each command has a permission"
            "level.\n\n"
            "\t-\t Help [PL=0] : ((PREFIX)Help) -> Displays the manual.\n\n")
