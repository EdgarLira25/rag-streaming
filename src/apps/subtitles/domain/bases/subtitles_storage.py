from abc import ABC, abstractmethod
from typing import Optional

from src.apps.subtitles.types.models import MediaType


class SubtitlesAbstractStorage(ABC):

    @abstractmethod
    async def get_subtitle(
        self,
        media_type: MediaType,
        location: str,
    ) -> bytes: ...

    @abstractmethod
    async def list_subtitles(
        self,
        media_type: MediaType,
        title: str,
        season: Optional[str],
        episode: Optional[str],
    ) -> list[str]: ...

    @abstractmethod
    async def add_subtitle(
        self,
        media_type: MediaType,
        title: str,
        season: Optional[str],
        episode: Optional[str],
        file: bytes,
        filename: str,
    ): ...
