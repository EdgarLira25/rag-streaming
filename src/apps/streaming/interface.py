from fastapi import APIRouter, Request
from src.apps.streaming.application import StreamingApplication

stream_router = APIRouter(prefix="/stream", tags=["Streaming"])


@stream_router.get("/watch")
async def stream(request: Request):
    return await StreamingApplication().stream(dict(request.headers))
