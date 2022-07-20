from typing import List

from fastapi import FastAPI, Depends, status

from dependencies import get_db
from schemas import PersonRequestSchema, PersonResponseSchema
from models import Person


app = FastAPI(dependencies=[Depends(get_db)])


@app.post("/persons", response_model=PersonResponseSchema)
def create_person(person_body: PersonRequestSchema):
    """
    создание персоны
    """

    person = Person.create(
        first_name=person_body.first_name,
        last_name=person_body.last_name,
        age=person_body.age,
        is_ill=person_body.is_ill,
        eye=person_body.eye,
    )

    response = PersonResponseSchema.from_orm(person)

    return response


@app.get("/persons/{person_id}", response_model=PersonResponseSchema)
def get_person(person_id: int):
    """
    получение конкретной персоны
    """

    person = Person.get_by_id(person_id)

    response = PersonResponseSchema.from_orm(person)

    return response


@app.get("/persons", response_model=List[PersonResponseSchema])
def get_person_list():
    """
    получение списка персон
    """

    person_list = Person.select()

    response = [PersonResponseSchema.from_orm(item) for item in person_list]

    return response


@app.delete("/persons/{person_id}", status_code=status.HTTP_200_OK)
def delete_person(person_id: int):
    """
    удаление персоны
    """

    person = Person.get_by_id(person_id)

    person.delete_instance()

    return {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
