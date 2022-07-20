from pydantic import BaseModel, validator


class PersonRequestSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_ill: bool
    eye: str

    @validator("age")
    def not_too_young(cls, value: int):
        if value <= 20:
            raise ValueError("too-young")

        return value


class PersonResponseSchema(PersonRequestSchema):
    id: int

    class Config:
        orm_mode = True
