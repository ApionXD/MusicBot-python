import json


class Settings:
    _prefix = "!"

    def __str__(self):
        var_dict = {
            "prefix": self._prefix
        }
        return json.dumps(var_dict)