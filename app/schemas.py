from pydantic import BaseModel


class PersonSchema(BaseModel):
    first_name: str
    last_name: str
    age: int
    is_ill: bool
    eye: str
