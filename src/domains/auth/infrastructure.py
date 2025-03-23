from sqlalchemy import select
from src.domains.auth.types.exceptions import UserNotFound
from src.domains.auth.types.models import UserInfo
from src.domains.shared.database.connector import Database
from src.domains.shared.database.daos.user import UserDao


class AuthRepository:

    user = UserDao

    def __init__(self, database_provider=Database()) -> None:
        self.db = database_provider

    def get_secret_hash(self, email: str) -> str:
        if result := self.db.select_one(
            select(self.user.secret_hash).where(self.user.email == email)
        ):
            return result["secret_hash"]

        raise UserNotFound()

    def get_user_info(self, email: str) -> UserInfo:
        if user := self.db.select_one(
            select(
                self.user.email,
                self.user.user_type,
                self.user.created_at,
                self.user.name,
            ).where(self.user.email == email)
        ):
            return UserInfo(
                email=user["email"],
                name=user["name"],
                user_type=user["user_type"],
                created_at=user["created_at"],
            )
        raise UserNotFound()
