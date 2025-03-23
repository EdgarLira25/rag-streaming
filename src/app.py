from fastapi import FastAPI
from src.domains.user.interface import user_router
from src.domains.auth.interface import auth_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
