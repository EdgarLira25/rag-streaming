from fastapi import APIRouter, HTTPException, status
from src.apps.user.interface.injection import UserInjection
from src.apps.user.types.models import CreateUserPayload


user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post(
    "",
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: CreateUserPayload,
    user_application: UserInjection,
):
    if not await user_application.create_user(user):
        raise HTTPException(detail={"error": "Email Already Used"}, status_code=409)
    return {"msg": "Registration Success"}
