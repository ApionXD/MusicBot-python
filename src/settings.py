import json
import os

settings_map = {

}


def load_settings(guild_list):
    for g in guild_list:
        settings_file_name = f"settings/{g.id}.json"
        if os.path.exists(settings_file_name):
            settings_file = open(settings_file_name)
            settings_json = settings_file.read()
            guild_settings = Settings.from_json(settings_json)
            settings_file.close()
            settings_map[g.id] = guild_settings
        else:
            print(f"Settings file for {g.name} not found! Creating one now")
            guild_settings = Settings()
            if not os.path.exists("settings/"):
                os.mkdir("settings")
            settings_file = open(settings_file_name, 'w')
            settings_file.write(guild_settings.to_json())
            settings_file.close()
            settings_map[g.id] = guild_settings

def save_settings(guild_id):
    settings_file_name = f"settings/{guild_id}.json"
    guild_settings = settings_map[guild_id]
    settings_file = open(settings_file_name, 'w')
    settings_file.write(guild_settings.to_json())
    settings_file.close()

class Settings:
    def __init__(self):
        self.prefix = '!'

    def to_json(self):
        return json.dumps({
            "prefix": self.prefix
        }, indent=4)

    @staticmethod
    def from_json(j):
        setting_dict = json.loads(j)
        result = Settings()
        result.prefix = setting_dict['prefix']
        return result
