class CatalogApplication:

    async def get_movies(self):
        raise NotImplementedError()

    async def get_series(self):
        raise NotImplementedError()

    async def post_movies(self):
        raise NotImplementedError()

    async def post_series(self):
        raise NotImplementedError()
