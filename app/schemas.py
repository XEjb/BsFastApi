from typing import List
from pydantic import BaseModel
from datetime import date


class Gente(BaseModel):
    name: str


class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Gente]
    pages: int
