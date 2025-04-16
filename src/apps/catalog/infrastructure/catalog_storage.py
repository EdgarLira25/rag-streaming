from src.apps.catalog.domain.base.catalog_storage import CatalogAbstractStorage
from src.apps.shared.storage.manager import StorageService


class CatalogStorage(CatalogAbstractStorage):
    def __init__(self, storage_provider: StorageService) -> None:
        self.storage = storage_provider

    def list_movie_titles(self) -> set[str]:
        storage = self.storage.get_container("movies")
        return {item.split("/")[1] for item in storage.list_blobs()}

    def get_movie_image(self, title: str) -> str:
        return self.storage.get_container("movies").get_blob_base64(f"{title}/default")

    def list_series_titles(self) -> set[str]:
        storage = self.storage.get_container("series")
        return {item.split("/")[1] for item in storage.list_blobs()}

    def get_series_image(self, title: str) -> str:
        return self.storage.get_container("series").get_blob_base64(
            f"/{title}/default_image"
        )

    def list_seasons(self, title: str) -> list[list[str]]:
        "lista de [[numero_da_temporada, episodio], ...]"
        prefix = f"/{title}/seasons/"
        storage = self.storage.get_container("series")
        return [
            path.replace(prefix, "", 1).split("/", 1)
            for path in storage.list_blobs(prefix)
            if "/subs/" not in path
        ]
