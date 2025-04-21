from typing import Literal, Optional
from src.apps.subtitles.domain.bases.subtitles_service import SubtitlesAbstractService
from src.apps.subtitles.domain.bases.subtitles_storage import SubtitlesAbstractStorage
from src.apps.subtitles.types.models import MediaType, SubLanguage, SubList


class SubtitlesUseCases:
    def __init__(
        self,
        subtitle_storage_provider: SubtitlesAbstractStorage,
        substitle_service_provider: SubtitlesAbstractService,
    ) -> None:
        self.subtitle_storage = subtitle_storage_provider
        self.subtitle_service = substitle_service_provider

    async def get_subtitle(
        self, media_type: Literal["movies", "series"], location: str
    ) -> bytes:
        return await self.subtitle_storage.get_subtitle(media_type, location)

    async def list_subtitles(
        self,
        media_type: Literal["movies", "series"],
        title: str,
        season: Optional[str],
        episode: Optional[str],
    ):
        return await self.subtitle_storage.list_subtitles(
            media_type, title, season, episode
        )

    async def add_subtitle(
        self,
        media_type: Literal["movies", "series"],
        title: str,
        season: Optional[str],
        episode: Optional[str],
        file: bytes,
        filename: str,
    ):
        await self.subtitle_storage.add_subtitle(
            media_type,
            title,
            season,
            episode,
            file,
            filename,
        )

    async def downloadable_subtitles(
        self, title: str, languages: SubLanguage
    ) -> list[SubList]:
        return sorted(
            await self.subtitle_service.downloadable_subtitles(title, languages),
            key=lambda sub: sub.download_count,
            reverse=True,
        )

    async def download_subtitle(
        self,
        sub_id: int,
        media_type: MediaType,
        title: str,
        season: Optional[str],
        episode: Optional[str],
    ):
        await self.subtitle_storage.add_subtitle(
            media_type=media_type,
            title=title,
            season=season,
            episode=episode,
            file=await self.subtitle_service.download_subtitle(sub_id),
            filename=str(sub_id) + ".srt",
        )
