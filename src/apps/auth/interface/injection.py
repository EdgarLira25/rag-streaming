from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from src.apps.auth.application.use_cases import AuthUseCases
from src.apps.auth.domain.auth_manager import AuthManager
from src.apps.auth.infrastructure.auth_repository import AuthRepository
from src.apps.shared.database.connector import Database


@lru_cache
def auth_injection() -> AuthUseCases:
    database = Database()
    auth_domain = AuthManager()
    auth_repository = AuthRepository(database_provider=database)
    return AuthUseCases(auth_domain=auth_domain, auth_repository=auth_repository)


AuthInjection = Annotated[AuthUseCases, Depends(auth_injection)]
