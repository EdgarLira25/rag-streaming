from typing import Optional
from src.apps.shared.storage.manager import StorageService
from src.apps.subtitles.domain.bases.subtitles_storage import SubtitlesAbstractStorage
from src.apps.subtitles.types.models import MediaType


class SubtitlesStorage(SubtitlesAbstractStorage):

    def __init__(self, storage_provider: StorageService) -> None:
        self.storage = storage_provider

    async def get_subtitle(self, media_type: MediaType, location: str) -> bytes:
        return self.storage.get_container(media_type).get_blob(location)

    async def list_subtitles(
        self,
        media_type: MediaType,
        title: str,
        season: Optional[str],
        episode: Optional[str],
    ):
        path = (
            f"/{title}/subs/"
            if media_type == "movies"
            else f"/{title}/seasons/{season}/{episode}/subs/"
        )
        return self.storage.get_container(media_type).list_blobs(path)

    async def add_subtitle(
        self,
        media_type: MediaType,
        title: str,
        season: Optional[str],
        episode: Optional[str],
        file: bytes,
        filename: str,
    ):
        path = (
            f"/{title}/subs/"
            if media_type == "movies"
            else f"/{title}/seasons/{season}/{episode}/subs/"
        )
        self.storage.get_container(media_type).create_blob(path + filename, file)
