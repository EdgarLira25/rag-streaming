import requests
from src.settings import (
    OPEN_SUBTITLE_API_KEY,
    OPEN_SUBTITLE_PASSWORD,
    OPEN_SUBTITLE_USERNAME,
)

TIMEOUT = 15


class OpenSubtitle:
    def __init__(self) -> None:
        self.base_url = "https://api.opensubtitles.com/api/v1"
        self._header = {
            "Api-Key": OPEN_SUBTITLE_API_KEY,
            "Authorization": "",
            "User-Agent": "rag-streaming/0.0.0",
        }
        self._bearer = ""

    @property
    def auth_headers(self):
        self._header["Authorization"] = requests.post(
            self.base_url + "/login",
            headers=self._header,
            timeout=TIMEOUT,
            json={
                "username": OPEN_SUBTITLE_USERNAME,
                "password": OPEN_SUBTITLE_PASSWORD,
            },
        ).json()["token"]
        return self._header

    def list_subtitles(self, movie_name: str, languages: str) -> dict:
        result = requests.get(
            self.base_url + "/subtitles",
            headers=self.auth_headers,
            params={"query": movie_name, "languages": languages},
            timeout=TIMEOUT,
        )
        return result.json() if result.ok else {}

    def download_sub(self, subtitle_id: int) -> dict:
        result = requests.post(
            self.base_url + "/download",
            headers=self.auth_headers,
            json={"file_id": subtitle_id},
            timeout=TIMEOUT,
        )
        return result.json() if result.ok else {}
