from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from src.domains.auth.application import AuthApplication
from src.domains.auth.types.models import AuthUser, RefreshToken
from src.domains.auth.types.exceptions import (
    AuthenticationFail,
    InvalidToken,
    UserNotFound,
)

auth_router = APIRouter(prefix="/auth", tags=["Authentication"])


@auth_router.post("/token")
async def token(
    body: AuthUser, auth_application: AuthApplication = Depends(AuthApplication)
) -> JSONResponse:
    try:
        return JSONResponse(content=await auth_application.token(body), status_code=200)
    except (UserNotFound, AuthenticationFail) as e:
        return JSONResponse(content=str(e), status_code=401)


@auth_router.post("/refresh_token")
async def refresh_token(
    body: RefreshToken, auth_application: AuthApplication = Depends(AuthApplication)
) -> JSONResponse:
    try:
        return JSONResponse(
            content=await auth_application.refresh_token(body.refresh_token),
            status_code=200,
        )
    except (InvalidToken, InvalidTokenError, ExpiredSignatureError, UserNotFound) as e:
        return JSONResponse(content=str(e), status_code=401)
