class Command:
    def __init__(self):
        # This is the default permission level for a command
        self.perm_level = 1000
    def run_command(self, command_event):
        print("This is just the general command! please subclass command and override run_command()"
              " to give functionality to a command")