from commands.command import Command


class Help(Command):
    perm_level = 0

    async def run_command(self, command_event):
        await command_event.message_event.channel.send(
            "-------------------------------- Discord Music Bot Manual ---------------------------------\n\n"
            "\t-\t Hello [PL=0] : ((PREFIX)hello) -> Prints \'Hello\' {username}!\n\n"
            "\t-\t Help [PL=0] : ((PREFIX)help) -> Displays this Help manual.\n\n"
            "\t-\t Get Permissions [PL=0] : ((PREFIX)getperms) -> This command returns the permission level (PL).\n\n"
            "\t-\t Play [PL=1000] : ((PREFIX)play [query]) -> Prompts bot to join a \n\n"
            "\t-\t Pause [PL=1000] : ((PREFIX)pause) -> Pauses the current song playing.\n\n"
            "\t-\t Resume [PL=1000] : ((PREFIX)resume) -> Resumes the paused song.\n\n"
            "\t-\t Queue [PL=1000] : ((PREFIX)queue [query]) -> This command takes the song specified by the user from the URL provided "
            "and appends it to a list. When the current song playing finishes, the first song in the queue will play.\n\n"
            "\t-\t Skip [PL=1000] : ((PREFIX)skip) -> This command terminates the current song playing. \n\n"
            "\t-\t Leave [PL=1000] : ((PREFIX)leave) -> This command removes the bot from its the current voice channel, stopping "
            "it from playing.\n\n"
            "\t-\t Set Prefix [PL=5000] : ((PREFIX)setprefix PREFIX) -> This command changes the prefix to enter a command. Once "
            "changed, to enter a command users must first enter the new prefix followed by their desired command.\n\n"
            "\t-\t Set Role Permissions [PL=5000] : ((PREFIX)setpermr [role] [pl]) -> Changes the permisson levels of roles in the server.\n\n"
            "\t-\t Set User Permissions [PL=5000] : ((PREFIX)setpermu [user] [pl]) -> Changes the permisson levels of users in the server.\n\n"
        )

