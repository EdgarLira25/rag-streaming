from src.apps.user.domain import UserDomain
from src.apps.user.infrastructure import UserRepository
from src.apps.user.types.models import CreateUserPayload


class UserApplication:
    def __init__(
        self,
        user_domain=UserDomain(),
        user_repository=UserRepository(),
    ) -> None:
        self.user_domain: UserDomain = user_domain
        self.user_repository: UserRepository = user_repository

    async def create_user(self, user: CreateUserPayload) -> bool:
        secret_hash = self.user_domain.get_secret_hash(user.email, user.password)
        return self.user_repository.create_user(
            email=user.email, secret_hash=secret_hash, name=user.email
        )
