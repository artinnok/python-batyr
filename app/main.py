from typing import List

from fastapi import FastAPI, Depends, status

from dependencies import get_db, get_queue
from schemas import PersonRequestSchema, PersonResponseSchema, PersonOptionalRequestSchema
from models import Person
from tasks import hello_world
from beat import create_schedule


app = FastAPI(dependencies=[Depends(get_db)], on_startup=[create_schedule])


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


@app.patch("/persons/{person_id}", response_model=PersonResponseSchema)
def update_person(person_id: int, person_body: PersonOptionalRequestSchema):
    """
    обновление персоны
    """

    person = Person.get_by_id(person_id)

    for key, value in person_body.dict(exclude_unset=True).items():
        setattr(person, key, value)

    person.save()

    response = PersonResponseSchema.from_orm(person)

    return response


@app.post("/run-task")
def run_task():
    """
    запуск задачи
    """

    queue = get_queue()
    queue.enqueue(hello_world)

    return {}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
