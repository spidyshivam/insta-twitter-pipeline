from fastapi import FastAPI
from app.routes.api import router

app = FastAPI(title="Instagram to Twitter API")

app.include_router(router)

@app.get("/")
def health_check():
    return {"message": "API is running!"}
