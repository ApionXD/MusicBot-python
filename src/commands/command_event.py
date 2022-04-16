class CommandEvent:
    def __init__(self, message_event, guild_settings):
        self.message_event = message_event
        self.words = message_event.content[1:].split()
        self.guild_settings = guild_settings
