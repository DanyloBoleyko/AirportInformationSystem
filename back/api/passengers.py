from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body
from starlette.responses import Response

from back.models import Employee, Task1, Task2, Task3, Profession, TablesEnum, Brigade, Passenger
from back.sql_server_client.client import db

router = APIRouter(
    prefix="/passengers",
    tags=["passengers"],
)


@router.get("/list")
async def get_passengers(
        passenger_id: Optional[int] = None
):
    params = {}
    if passenger_id:
        params['passenger_id'] = passenger_id
    return db.select(TablesEnum.Passenger, params)


@router.post("/add")
async def add_passenger(
        data: dict = Body(...)
):
    passenger = Passenger(**{
        **data
    })

    db.insert(passenger)

    return Response(status_code=201, content='Passenger created')

