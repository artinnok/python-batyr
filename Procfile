web: uvicorn app.main:app --host=0.0.0.0 --port=${PORT}
worker: rq worker -c app.dependencies
