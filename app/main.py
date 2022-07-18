from fastapi import FastAPI, Depends
from dependencies import get_db
from schemas import PersonSchema


app = FastAPI(dependencies=[Depends(get_db)])


@app.post("/persons")
def create_person(person: PersonSchema) -> dict:
    return {"status": "hello"}


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
