from fastapi import FastAPI, Depends
from dependencies import get_db
from schemas import PersonRequestSchema, PersonResponseSchema
from models import Person


app = FastAPI(dependencies=[Depends(get_db)])


@app.post("/persons")
def create_person(person_body: PersonRequestSchema) -> dict:
    person = Person.create(
        first_name=person_body.first_name,
        last_name=person_body.last_name,
        age=person_body.age,
        is_ill=person_body.is_ill,
        eye=person_body.eye,
    )

    response = PersonResponseSchema.from_orm(person)

    return response.dict()


@app.get("/persons/{person_id}")
def get_person(person_id: int) -> dict:
    person = Person.get_by_id(person_id)

    response = PersonResponseSchema.from_orm(person)

    return response.dict()


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
