from src.apps.user.domain.user_hash import UserHash
from src.apps.user.infrastructure.user_repository import UserRepository
from src.apps.user.types.models import CreateUserPayload


class UserUseCases:
    def __init__(self, user_hasher: UserHash, user_repository: UserRepository) -> None:
        self.user_hasher = user_hasher
        self.user_repository = user_repository

    async def create_user(self, user: CreateUserPayload) -> bool:
        secret_hash = self.user_hasher.get_secret_hash(user.email, user.password)
        return self.user_repository.create_user(
            email=user.email, secret_hash=secret_hash, name=user.email
        )
