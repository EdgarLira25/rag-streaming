from fastapi import APIRouter
from src.domains.subtitles.application import SubtitlesApplication

subtitles_router = APIRouter(prefix="/subtitles", tags=["Subtitles"])


@subtitles_router.get("/{sub_id}")
async def get_subtitle(sub_id: int):
    return await SubtitlesApplication().get_subtitle(sub_id)


@subtitles_router.post("")
async def post_subtitle():
    return await SubtitlesApplication().add_subtitle()


@subtitles_router.get("/list")
async def get_all_subtitles():
    return await SubtitlesApplication().list_subtitles()


@subtitles_router.get("/downloadables")
async def post_movies():
    return await SubtitlesApplication().downloadable_subtitles()


@subtitles_router.get("/downloadables/{sub_id}")
async def post_series(sub_id: int):
    return await SubtitlesApplication().download_subtitle(sub_id)
