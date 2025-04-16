from pydantic import BaseModel


class Movies(BaseModel):
    title: str
    image: str


class Series(BaseModel):
    title: str
    image: str


class Seasons(BaseModel):
    title: str
    seasons: dict[str, list[str]]
