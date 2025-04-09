from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import APIRouter, HTTPException, status
from src.apps.auth.interface.injection import AuthInjection
from src.apps.auth.types.models import AuthUser, RefreshToken, Token
from src.apps.auth.types.exceptions import (
    AuthenticationFail,
    InvalidToken,
    UserNotFound,
)

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post("/token", response_model=Token, status_code=status.HTTP_200_OK)
async def token(body: AuthUser, auth_application: AuthInjection):
    try:
        return await auth_application.token(body)
    except (UserNotFound, AuthenticationFail) as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_401_UNAUTHORIZED
        ) from e


@auth_router.post(
    "/refresh_token", response_model=Token, status_code=status.HTTP_200_OK
)
async def refresh_token(body: RefreshToken, auth_application: AuthInjection):
    try:
        return await auth_application.refresh_token(body.refresh_token)
    except (InvalidToken, InvalidTokenError, ExpiredSignatureError, UserNotFound) as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_401_UNAUTHORIZED
        ) from e
