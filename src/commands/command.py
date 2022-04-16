class Command:
    # Default permission level required to run this command
    perm_level = 1000
    def run_command(self, command_event):
        print("This is just the general command! please subclass command and override run_command()"
              " to give functionality to a command")