from typing import Annotated
from fastapi import APIRouter, Body, Form, Query, status

from src.apps.subtitles.interface.injection import SubtitleInjection
from src.apps.subtitles.types.models import (
    DownloadablesSub,
    GetSubtitleParams,
    SubList,
    SubtitleBodyDownload,
    SubtitleFormData,
    SubtitleParams,
)

subtitles_router = APIRouter(prefix="/subtitles", tags=["Subtitles"])


@subtitles_router.get("")
async def get_subtitle(
    query: Annotated[GetSubtitleParams, Query()],
    subtitle_application: SubtitleInjection,
):
    return await subtitle_application.get_subtitle(query.media_type, query.location)


@subtitles_router.post("")
async def post_subtitle(
    form: Annotated[SubtitleFormData, Form()], subtitle_application: SubtitleInjection
):
    return await subtitle_application.add_subtitle(
        media_type=form.media_type,
        title=form.title,
        season=form.season,
        episode=form.episode,
        file=form.file,
        filename=form.filename,
    )


@subtitles_router.get("/list")
async def get_all_subtitles(
    query: Annotated[SubtitleParams, Query()],
    subtitle_application: SubtitleInjection,
):
    return await subtitle_application.list_subtitles(
        media_type=query.media_type,
        episode=query.episode,
        season=query.season,
        title=query.title,
    )


@subtitles_router.get(
    "/downloadables", response_model=list[SubList], status_code=status.HTTP_200_OK
)
async def list_downloadables_subs(
    query: Annotated[DownloadablesSub, Query()], subtitle_application: SubtitleInjection
):
    return await subtitle_application.downloadable_subtitles(
        query.title, query.language
    )


@subtitles_router.post("/downloadables", status_code=status.HTTP_201_CREATED)
async def download_sub(
    body: Annotated[SubtitleBodyDownload, Body()],
    subtitle_application: SubtitleInjection,
):
    await subtitle_application.download_subtitle(
        sub_id=body.sub_id,
        media_type=body.media_type,
        episode=body.episode,
        season=body.season,
        title=body.title,
    )
    return {"msg": "legenda baixada com sucesso"}
