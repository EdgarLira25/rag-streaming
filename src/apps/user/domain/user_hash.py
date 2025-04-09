import hashlib


class UserHash:

    def get_secret_hash(self, email: str, password: str):
        return hashlib.sha256(f"{email}{password}".encode()).hexdigest()
