from datetime import UTC, datetime, timedelta
import hashlib
import jwt
from src.apps.auth.types.exceptions import AuthenticationFail, InvalidToken
from src.apps.auth.types.models import UserInfo
from src.settings import ALGORITHM, REFRESH_TOKEN_TIME, SECRET_KEY, TOKEN_TIME


class AuthDomain:
    def check_secret_hash(self, email: str, password: str, secret_hash: str) -> None:
        if not hashlib.sha256(f"{email}{password}".encode()).hexdigest() == secret_hash:
            raise AuthenticationFail("Invalid Password")

    def create_access_token(self, user: UserInfo):
        expire = datetime.now(UTC) + timedelta(seconds=TOKEN_TIME)
        data = {
            "exp": expire,
            "email": user.email,
            "user_type": user.user_type,
            "type": "access",
        }
        return jwt.encode(payload=data, key=SECRET_KEY, algorithm=ALGORITHM)

    def create_refresh_token(self, user: UserInfo):
        expire = datetime.now(UTC) + timedelta(REFRESH_TOKEN_TIME)
        encoded_jwt = jwt.encode(
            payload={"exp": expire, "email": user.email, "type": "refresh"},
            key=SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return encoded_jwt

    def check_refresh_token(self, token: str) -> None:
        "Check if is valid else raise ExpiredSignatureError or InvalidTokenError or InvalidToken"
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        if payload["type"] != "refresh":
            raise InvalidToken("Invalid access token")

    def check_token(self, token: str) -> None:
        "Check if is valid else raise ExpiredSignatureError or InvalidTokenError or InvalidAccessToken"
        payload = jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
        if payload["type"] != "access":
            raise InvalidToken("Invalid refresh token")

    def decode_token(self, token: str) -> dict:
        return jwt.decode(jwt=token, key=SECRET_KEY, algorithms=[ALGORITHM])
