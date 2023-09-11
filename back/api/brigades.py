from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body
from starlette.responses import Response

from back.models import Employee, Task1, Task2, Task3, Profession, TablesEnum, Brigade
from back.sql_server_client.client import db

router = APIRouter(
    prefix="/brigades",
    tags=["brigades"],
)


@router.get("/list")
async def get_brigades(
        brigade_id: Optional[int] = None,
        department_id: Optional[int] = None,
):
    params = {}
    if brigade_id:
        params['brigade_id'] = brigade_id
    if department_id:
        params['department_id'] = department_id
    return db.select(TablesEnum.Brigade, params)


@router.post("/add")
async def add_brigade(
        data: dict = Body(...)
):
    department = db.select(TablesEnum.Department, {'name': data['department']})
    if not department:
        return Response(status_code=400, content='Department not found')

    brigade = Brigade(**{
        **data,
        'department_id': department[0]['department_id']
    })

    db.insert(brigade)

    return Response(status_code=201, content='Brigade created')

