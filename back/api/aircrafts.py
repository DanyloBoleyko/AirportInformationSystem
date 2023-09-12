from datetime import datetime
from typing import Optional

from fastapi import APIRouter

from back.models import Task4, TablesEnum
from back.sql_server_client import db

router = APIRouter(
    prefix="/aircrafts",
    tags=["aircrafts"],
)


@router.get("/list")
async def get_aircrafts(
        aircraft_id: Optional[int] = None,
        aircraft_type_id: Optional[int] = None,
        with_types: Optional[bool] = False
):
    params = {}
    join = {}
    if aircraft_id:
        params['aircraft_id'] = aircraft_id
    if aircraft_type_id:
        params['aircraft_type_id'] = aircraft_type_id
    if with_types:
        join[TablesEnum.AircraftType] = 'aircraft_type_id'

    return db.select(TablesEnum.Aircraft, params, join)


@router.get("/type/list")
async def get_aircraft_types(
        aircraft_type_id: Optional[int] = None,
):
    params = {}
    if aircraft_type_id:
        params['aircraft_type_id'] = aircraft_type_id
    return db.select(TablesEnum.AircraftType, params)


@router.get("/in_airport")
async def get_aircrafts_in_airport(
        airport_id: Optional[int] = None,
        datetime_range_start: Optional[datetime] = None,
        datetime_range_end: Optional[datetime] = None,
):
    """
    Одержати перелік і загальну кількість літаків приписаних до аеропорту, що знаходяться в ньому у вказаний час,
    за часом прильоту до аеропорту, за кількістю здійснених рейсів.
    """
    rows = db.procedure(Task4(
        airport_id=airport_id,
        datetime_range_start=datetime_range_start,
        datetime_range_end=datetime_range_end
    ))
    return rows
