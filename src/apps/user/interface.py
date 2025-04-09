from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from src.apps.user.application import UserApplication
from src.apps.user.types.models import CreateUserPayload


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("")
async def create_user(
    user: CreateUserPayload,
    user_application: UserApplication = Depends(UserApplication),
):
    if not await user_application.create_user(user):
        raise HTTPException(detail={"error": "Usuário já cadastrado"}, status_code=409)
    return JSONResponse(content={"msg": "Registration Success"}, status_code=200)
