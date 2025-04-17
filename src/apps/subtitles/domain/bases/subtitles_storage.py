from abc import ABC, abstractmethod


class SubtitlesAbstractStorage(ABC):

    @abstractmethod
    async def get_subtitle(self, sub_id: int): ...

    @abstractmethod
    async def list_subtitles(self): ...

    @abstractmethod
    async def add_subtitle(self): ...
