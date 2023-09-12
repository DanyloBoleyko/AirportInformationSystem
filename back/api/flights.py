from typing import Optional

from fastapi import APIRouter

from back.models import TablesEnum, Task6
from back.sql_server_client import db

router = APIRouter(
    prefix="/flights",
    tags=["flights"],
)


@router.get("/list")
async def get_flights(
        flight_id: Optional[int] = None,
        aircraft_id: Optional[int] = None,
        from_airport_id: Optional[int] = None,
        to_airport_id: Optional[int] = None,
        with_schedule: Optional[bool] = None,
        with_route: Optional[bool] = None,
):
    params = {}
    if flight_id:
        params['flight_id'] = flight_id
    if from_airport_id:
        params['from_airport_id'] = from_airport_id
    if to_airport_id:
        params['to_airport_id'] = to_airport_id
    if aircraft_id:
        params['aircraft_id'] = aircraft_id

    join = {}
    if with_schedule:
        join[TablesEnum.Schedule] = 'schedule_id'
    if with_route:
        join[TablesEnum.FlightRoute] = 'flight_id'

    return db.select(TablesEnum.Flight, params, join)


@router.get("/route/list")
async def get_flight_by_route(
        from_airport: Optional[int] = None,
        to_airport: Optional[int] = None,
):
    return db.procedure(Task6(
        from_airport=from_airport,
        to_airport=to_airport
    ))


@router.get("/schedule/list")
async def get_flight_schedule(
        schedule_id: Optional[int] = None,
):
    params = {}
    if schedule_id:
        params['schedule_id'] = schedule_id
    return db.select(TablesEnum.Schedule, params)
