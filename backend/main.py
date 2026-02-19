from fastapi import FastAPI
from api.routes import router
from database.init_db import init_db
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Women Safety IoT Backend")

init_db()

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "Backend running"}
