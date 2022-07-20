from typing import Optional
from pydantic import BaseModel, validator


MINIMUM_YEAR = 20


class PersonRequestSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_ill: bool
    eye: str

    @validator("age")
    def not_too_young(cls, value: int):
        if value < MINIMUM_YEAR:
            raise ValueError("you are too young")

        return value


class PersonResponseSchema(PersonRequestSchema):
    id: int

    class Config:
        orm_mode = True


class PersonOptionalRequestSchema(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    is_ill: Optional[bool]
    eye: Optional[str]

    @validator("age")
    def not_too_young(cls, value: int):
        if value <= 20:
            raise ValueError("too-young")

        return value
