from fastapi import APIRouter
from src.apps.catalog.application import CatalogApplication

catalog_router = APIRouter(prefix="/catalog", tags=["Catalog"])


@catalog_router.get("/movies")
async def get_movies():
    return await CatalogApplication().get_movies()


@catalog_router.get("/series")
async def get_series():
    return await CatalogApplication().get_series()


@catalog_router.post("/movies")
async def post_movies():
    return await CatalogApplication().post_movies()


@catalog_router.post("/series")
async def post_series():
    return await CatalogApplication().post_series()
