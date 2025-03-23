from sqlalchemy import insert
from sqlalchemy.exc import IntegrityError
from src.domains.shared.database.connector import Database
from src.domains.shared.database.daos.user import UserDao


class UserRepository:

    user = UserDao

    def __init__(self, database_provider=Database()) -> None:
        self.db: Database = database_provider

    def create_user(self, email: str, secret_hash: str, name: str) -> bool:
        try:
            self.db.statement(
                insert(self.user).values(
                    email=email, secret_hash=secret_hash, name=name
                )
            )
            return True
        except IntegrityError:
            return False
