from collections import defaultdict
from src.apps.catalog.infrastructure.catalog_storage import CatalogStorage
from src.apps.catalog.types.models import Movies, Seasons, Series


class CatalogUseCases:
    def __init__(self, storage_provider: CatalogStorage) -> None:
        self.catalog_storage = storage_provider

    async def get_all_movies(self) -> list[Movies]:
        return [
            Movies(
                title=title,
                image=self.catalog_storage.get_movie_image(title),
            )
            for title in self.catalog_storage.list_movie_titles()
        ]

    async def get_all_series(self) -> list[Series]:
        return [
            Series(
                title=title,
                image=self.catalog_storage.get_series_image(title),
            )
            for title in self.catalog_storage.list_series_titles()
        ]

    async def get_seasons(self, title: str) -> Seasons:
        seasons_dict = defaultdict(list)
        for seasons in self.catalog_storage.list_seasons(title):
            seasons_dict[seasons[0]].append(seasons[1])

        return Seasons(title=title, seasons=seasons_dict)
