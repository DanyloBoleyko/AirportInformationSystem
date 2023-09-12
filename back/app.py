from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from back.api.employees import router as employees_router
from back.api.departments import router as departments_router
from back.api.aircrafts import router as aircrafts_router
from back.api.professions import router as professions_router
from back.api.brigades import router as brigades_router
from back.api.flights import router as flights_router
from back.api.passengers import router as passengers_router
from back.api.airports import router as airports_router
from back.api.tickets import router as tickets_router

app = FastAPI(title="AirportInformationSystem API")

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
app.include_router(flights_router)
app.include_router(passengers_router)
app.include_router(passengers_router)
app.include_router(airports_router)
app.include_router(tickets_router)
