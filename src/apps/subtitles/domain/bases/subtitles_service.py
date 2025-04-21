from abc import ABC, abstractmethod
from src.apps.subtitles.types.models import SubLanguage, SubList


class SubtitlesAbstractService(ABC):

    @abstractmethod
    async def downloadable_subtitles(
        self, media_name: str, languages: SubLanguage
    ) -> list[SubList]: ...

    @abstractmethod
    async def download_subtitle(self, sub_id: int) -> bytes: ...
