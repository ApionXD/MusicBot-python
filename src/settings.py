import json


class Settings:
    def __init__(self):
        self.prefix = '!'

    def to_json(self):
        return json.dumps({
            "prefix": self.prefix
        }, indent=4)
