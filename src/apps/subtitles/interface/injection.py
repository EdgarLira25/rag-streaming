from functools import lru_cache
from typing import Annotated

from fastapi import Depends

from src.apps.shared.open_subtitles.client import OpenSubtitle
from src.apps.shared.storage.manager import StorageService
from src.apps.subtitles.application.use_cases import SubtitlesUseCases
from src.apps.subtitles.infrastructure.substitles_service import SubtitlesService
from src.apps.subtitles.infrastructure.subtitles_storage import SubtitlesStorage


@lru_cache
def subtitle_injection() -> SubtitlesUseCases:
    storage_service = StorageService()
    open_subtitle = OpenSubtitle()
    subtitle_service = SubtitlesService(open_subtitle)
    subtitle_storage = SubtitlesStorage(storage_service)

    return SubtitlesUseCases(
        subtitle_storage_provider=subtitle_storage,
        substitle_service_provider=subtitle_service,
    )


SubtitleInjection = Annotated[SubtitlesUseCases, Depends(subtitle_injection)]
