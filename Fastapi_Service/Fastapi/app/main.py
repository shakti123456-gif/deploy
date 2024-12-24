from typing import List
from pydantic import BaseModel, HttpUrl
from app.quotes.examples import ex_author, ex_quote, ex_tag


class Author(BaseModel):
    name: str
    url: HttpUrl

    class Config:
        schema_extra = {"example": ex_author}


class Tag(BaseModel):
    name: str
    url: HttpUrl

    class Config:
        schema_extra = {"example": ex_tag}


class Quote(BaseModel):
    text: str
    author: Author
    tags: List[Tag]

    class Config:
        schema_extra = {"example": ex_quote}