from fastapi import FastAPI, Depends
from dependencies import get_db


app = FastAPI(dependencies=[Depends(get_db)])


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
