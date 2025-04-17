from src.apps.subtitles.domain.bases.subtitles_service import SubtitlesAbstractService
from src.apps.subtitles.domain.bases.subtitles_storage import SubtitlesAbstractStorage


class SubtitlesUseCases:
    def __init__(
        self,
        subtitle_storage_provider: SubtitlesAbstractStorage,
        substitle_service_provider: SubtitlesAbstractService,
    ) -> None:
        self.subtitle_storage = subtitle_storage_provider
        self.subtitle_service = substitle_service_provider

    async def get_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()

    async def list_subtitles(self):
        raise NotImplementedError()

    async def add_subtitle(self):
        raise NotImplementedError()

    async def downloadable_subtitles(self):
        raise NotImplementedError()

    async def download_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()
