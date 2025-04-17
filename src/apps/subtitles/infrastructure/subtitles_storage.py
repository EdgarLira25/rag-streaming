from src.apps.shared.storage.manager import StorageService
from src.apps.subtitles.domain.bases.subtitles_storage import SubtitlesAbstractStorage


class SubtitlesStorage(SubtitlesAbstractStorage):

    def __init__(self, storage_provider: StorageService) -> None:
        self.storage = storage_provider

    async def get_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()

    async def list_subtitles(self):
        raise NotImplementedError()

    async def add_subtitle(self):
        raise NotImplementedError()
