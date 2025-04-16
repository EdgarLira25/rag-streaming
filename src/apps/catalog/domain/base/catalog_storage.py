from abc import ABC, abstractmethod

# pyling: ignore


class CatalogAbstractStorage(ABC):

    @abstractmethod
    def list_movie_titles(self) -> set[str]: ...

    @abstractmethod
    def get_movie_image(self, title: str) -> str: ...

    @abstractmethod
    def list_series_titles(self) -> set[str]: ...

    @abstractmethod
    def get_series_image(self, title: str) -> str: ...

    @abstractmethod
    def list_seasons(self, title: str) -> list[list[str]]: ...
