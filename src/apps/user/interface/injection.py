from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from src.apps.shared.database.connector import Database
from src.apps.user.application.use_cases import UserUseCases
from src.apps.user.domain.user_hash import UserHash
from src.apps.user.infrastructure.user_repository import UserRepository


@lru_cache
def user_injection() -> UserUseCases:
    database = Database()
    user_hasher = UserHash()
    user_repository = UserRepository(database_provider=database)
    return UserUseCases(user_hasher=user_hasher, user_repository=user_repository)


UserInjection = Annotated[UserUseCases, Depends(user_injection)]
