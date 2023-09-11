from datetime import datetime
from typing import Optional

from fastapi import APIRouter

from back.models import Task4, TablesEnum
from back.sql_server_client import db

router = APIRouter(
    prefix="/flights",
    tags=["flights"],
)


@router.get("/list")
async def get_flights(
        flight_id: Optional[int] = None,
        from_airport_id: Optional[int] = None,
        to_airport_id: Optional[int] = None,
):
    params = {}
    if flight_id:
        params['flight_id'] = flight_id
    if from_airport_id:
        params['from_airport_id'] = from_airport_id
    if to_airport_id:
        params['to_airport_id'] = to_airport_id
    return db.select(TablesEnum.Flight, params)

