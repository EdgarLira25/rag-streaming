from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from src.apps.user.interface.router import user_router
from src.apps.auth.interface.router import auth_router
from src.apps.catalog.interface.router import catalog_router

app = FastAPI()
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(catalog_router)


@app.get("/")
def root():
    return RedirectResponse("/docs", status_code=status.HTTP_308_PERMANENT_REDIRECT)
