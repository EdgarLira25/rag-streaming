from typing import Literal, Optional, TypeAlias
from pydantic import BaseModel


MediaType: TypeAlias = Literal["movies", "series"]
SubLanguage: TypeAlias = Literal["en", "pt-BR", "es"]


class GetSubtitleParams(BaseModel):
    media_type: MediaType
    location: str


class SubtitleParams(BaseModel):
    media_type: MediaType
    title: str
    season: Optional[str] = None
    episode: Optional[str] = None


class SubtitleBodyDownload(SubtitleParams):
    sub_id: int


class SubtitleFormData(SubtitleParams):
    file: bytes
    filename: str


class DownloadablesSub(BaseModel):
    title: str
    language: SubLanguage


class SubList(BaseModel):
    id: str
    download_count: int
    language: SubLanguage
    release: str
