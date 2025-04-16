from functools import lru_cache
from typing import Annotated
from fastapi import Depends
from src.apps.catalog.application.use_cases import CatalogUseCases
from src.apps.catalog.infrastructure.catalog_storage import CatalogStorage
from src.apps.shared.storage.manager import StorageService


@lru_cache
def catalog_injection() -> CatalogUseCases:
    storage_service = StorageService()
    catalog_storage = CatalogStorage(storage_provider=storage_service)
    return CatalogUseCases(catalog_storage)


CatalogInjection = Annotated[CatalogUseCases, Depends(catalog_injection)]
