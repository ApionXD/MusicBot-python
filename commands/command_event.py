class CommandEvent:
    def __init__(self, message_event):
        self.message_event = message_event
        self.words = message_event.content[1:].split()
