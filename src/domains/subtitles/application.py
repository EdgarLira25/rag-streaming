class SubtitlesApplication:

    async def get_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()

    async def list_subtitles(self):
        raise NotImplementedError()

    async def add_subtitle(self):
        raise NotImplementedError()

    async def downloadable_subtitles(self):
        raise NotImplementedError()

    async def download_subtitle(self, sub_id: int):
        assert sub_id
        raise NotImplementedError()
