from pydantic import BaseModel


class PersonRequestSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_ill: bool
    eye: str


class PersonResponseSchema(PersonRequestSchema):
    id: int

    class Config:
        orm_mode = True
