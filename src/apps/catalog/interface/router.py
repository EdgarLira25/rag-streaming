from fastapi import APIRouter, status
from src.apps.catalog.interface.injection import CatalogInjection
from src.apps.catalog.types.models import Movies, Seasons, Series

catalog_router = APIRouter(prefix="/catalog", tags=["Catalog"])


@catalog_router.get(
    "/movies", response_model=list[Movies], status_code=status.HTTP_200_OK
)
async def get_movies(catalog_application: CatalogInjection):
    return await catalog_application.get_all_movies()


@catalog_router.get(
    "/series", response_model=list[Series], status_code=status.HTTP_200_OK
)
async def get_series(catalog_application: CatalogInjection):
    return await catalog_application.get_all_series()


@catalog_router.get(
    "/series/seasons", response_model=Seasons, status_code=status.HTTP_200_OK
)
async def get_seasons(title: str, catalog_application: CatalogInjection):
    return await catalog_application.get_seasons(title)
