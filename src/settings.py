import json
import os
import permission_map

settings_map = dict()


def load_settings(guild_list):
    for g in guild_list:
        settings_file_name = f"settings/{g.name}.json"
        if os.path.exists(settings_file_name):
            settings_file = open(settings_file_name)
            settings_json = settings_file.read()
            guild_settings = Settings.from_json(settings_json)
            settings_file.close()
            settings_map[g.id] = guild_settings
        else:
            print(f"Settings file for {g.name} not found! Creating one now")
            guild_settings = Settings.gen_default_settings(g)
            if not os.path.exists("settings/"):
                os.mkdir("settings")
            settings_file = open(settings_file_name, 'w')
            settings_file.write(guild_settings.to_json())
            settings_file.close()
            settings_map[g.id] = guild_settings


def save_settings(guild_id, guild_name):
    settings_file_name = f"settings/{guild_name}.json"
    guild_settings = settings_map[guild_id]
    settings_file = open(settings_file_name, 'w')
    settings_file.write(guild_settings.to_json())
    settings_file.close()


class Settings:
    def __init__(self):
        self.prefix = '!'

    @staticmethod
    def gen_default_settings(guild):
        result = Settings()
        result.prefix = '!'
        result.voice_channel_id = guild.voice_channels[0].id
        result.command_channel_id = guild.text_channels[0].id
        result.perm_map = permission_map.PermissionMap()
        result.perm_map.gen_default_perms(guild)
        return result

    def to_json(self):
        return json.dumps({
            "prefix": self.prefix,
            "voice_channel_id": self.voice_channel_id,
            "command_channel_id": self.command_channel_id,
            "permission_mappings": {"roles": self.perm_map.role_map, "users": self.perm_map.user_map}
        }, indent=4)

    @staticmethod
    def from_json(j):
        setting_dict = json.loads(j)
        result = Settings()
        result.prefix = setting_dict['prefix']
        result.voice_channel_id = setting_dict['voice_channel_id']
        result.command_channel_id = setting_dict['command_channel_id']
        result.perm_map = permission_map.PermissionMap.from_dict(setting_dict["permission_mappings"])
        return result
