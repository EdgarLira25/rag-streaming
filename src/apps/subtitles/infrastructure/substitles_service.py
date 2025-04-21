import requests
from src.apps.shared.open_subtitles.client import OpenSubtitle
from src.apps.subtitles.domain.bases.subtitles_service import SubtitlesAbstractService
from src.apps.subtitles.types.models import SubLanguage, SubList


class SubtitlesService(SubtitlesAbstractService):
    def __init__(self, subtitles_client_provider: OpenSubtitle) -> None:
        self.client = subtitles_client_provider

    async def downloadable_subtitles(self, media_name: str, languages: SubLanguage):
        subtitles = self.client.list_subtitles(media_name, languages)
        return [
            SubList(
                id=sub["id"],
                download_count=sub["attributes"]["download_count"],
                language=sub["attributes"]["language"],
                release=sub["attributes"]["release"],
            )
            for sub in subtitles["data"]
        ]

    async def download_subtitle(self, sub_id: int) -> bytes:
        return requests.get(
            self.client.download_sub(sub_id)["link"], timeout=10
        ).text.encode()
