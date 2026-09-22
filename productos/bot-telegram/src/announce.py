class Announcements:
    def __init__(self, config, logger):
        self.enabled = config.get("enabled", True)
        self.logger = logger

    def is_admin(self, user_id, admin_ids):
        return user_id in admin_ids

    def prepare(self, user_id, admin_ids, text):
        if not self.enabled:
            return None
        if not self.is_admin(user_id, admin_ids):
            return None
        cleaned = text.strip()
        if not cleaned:
            return None
        self.logger.log("announce", {"author": user_id, "length": len(cleaned)})
        return cleaned