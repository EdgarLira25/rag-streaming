from src.apps.shared.open_subtitles.client import OpenSubtitle
from src.apps.subtitles.domain.bases.subtitles_service import SubtitlesAbstractService


class SubtitlesService(SubtitlesAbstractService):
    def __init__(self, subtitles_client_provider: OpenSubtitle) -> None:
        self.client = subtitles_client_provider

    async def downloadable_subtitles(self):
        raise NotImplementedError()

    async def download_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()
