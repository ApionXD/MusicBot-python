class PermissionMap:
    def __init__(self):
        self.user_map = dict()
        self.role_map = dict()

    def get_highest_permission_level(self, member):
        result = 0
        if str(member.id) in self.user_map:
            result = self.user_map[str(member.id)]
        member_roles = member.roles
        for x in member_roles:
            if str(x.id) in self.role_map:
                perm_level = self.role_map[str(x.id)]
                if perm_level > result:
                    result = perm_level
        return result

    def gen_default_perms(self, guild):
        self.user_map[guild.owner_id] = 1000000

    @staticmethod
    def from_dict(d):
        result = PermissionMap()
        result.role_map = d["roles"]
        result.user_map = d["users"]
        return result
