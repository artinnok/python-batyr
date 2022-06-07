~/Desktop/evrone
from typing import List

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health() -> dict:
    return {"status": "okay"}
