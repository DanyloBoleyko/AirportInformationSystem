from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from back.api.employees import router as employees_router
from back.api.departments import router as departments_router
from back.api.aircrafts import router as aircrafts_router
from back.api.professions import router as professions_router
from back.api.brigades import router as brigades_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5050"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(employees_router)
app.include_router(departments_router)
app.include_router(aircrafts_router)
app.include_router(professions_router)
app.include_router(brigades_router)
