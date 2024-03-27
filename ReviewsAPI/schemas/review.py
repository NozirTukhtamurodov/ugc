from pydantic import BaseModel
from uuid import UUID
from pydantic import Field


class MarkFilmDto(BaseModel):
    film_id: UUID
    mark: int = Field(ge=0, le=10)


class MarkReviewDto(BaseModel):
    review_id: UUID
    mark: int = Field(ge=0, le=10)
    text: str


class CreateReviewDto(BaseModel):
    text: str
    film_id: UUID
