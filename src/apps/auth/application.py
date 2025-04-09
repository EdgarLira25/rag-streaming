from src.apps.auth.domain import AuthDomain
from src.apps.auth.infrastructure import AuthRepository
from src.apps.auth.types.models import AuthUser, Token, UserInfo


class AuthApplication:
    def __init__(
        self, auth_domain=AuthDomain(), auth_repository=AuthRepository()
    ) -> None:
        self.auth_domain: AuthDomain = auth_domain
        self.auth_repository: AuthRepository = auth_repository

    async def _gen_token(self, user_info: UserInfo):
        return Token(
            access_token=self.auth_domain.create_access_token(user_info),
            refresh_token=self.auth_domain.create_refresh_token(user_info),
        )

    async def token(self, user: AuthUser) -> Token:
        secret_hash = self.auth_repository.get_secret_hash(user.email)
        self.auth_domain.check_secret_hash(
            email=user.email, password=user.password, secret_hash=secret_hash
        )
        return await self._gen_token(self.auth_repository.get_user_info(user.email))

    async def refresh_token(self, token: str) -> Token:
        self.auth_domain.check_refresh_token(token)
        decoded_token = self.auth_domain.decode_token(token)
        user_info = self.auth_repository.get_user_info(decoded_token["email"])
        return await self._gen_token(user_info)
