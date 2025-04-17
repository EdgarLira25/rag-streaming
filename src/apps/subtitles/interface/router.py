from fastapi import APIRouter

from src.apps.subtitles.interface.injection import SubtitleInjection

subtitles_router = APIRouter(prefix="/subtitles", tags=["Subtitles"])


@subtitles_router.get("/{sub_id}")
async def get_subtitle(sub_id: int, subtitle_application: SubtitleInjection):
    return await subtitle_application.get_subtitle(sub_id)


@subtitles_router.post("")
async def post_subtitle(subtitle_application: SubtitleInjection):
    return await subtitle_application.add_subtitle()


@subtitles_router.get("/list")
async def get_all_subtitles(subtitle_application: SubtitleInjection):
    return await subtitle_application.list_subtitles()


@subtitles_router.get("/downloadables")
async def post_movies(subtitle_application: SubtitleInjection):
    return await subtitle_application.downloadable_subtitles()


@subtitles_router.get("/downloadables/{sub_id}")
async def post_series(sub_id: int, subtitle_application: SubtitleInjection):
    return await subtitle_application.download_subtitle(sub_id)
