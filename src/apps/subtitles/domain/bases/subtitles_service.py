from abc import ABC, abstractmethod


class SubtitlesAbstractService(ABC):

    @abstractmethod
    async def downloadable_subtitles(self): ...

    @abstractmethod
    async def download_subtitle(self, sub_id: int): ...
