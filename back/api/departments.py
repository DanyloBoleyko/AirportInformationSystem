from fastapi import APIRouter, Body
from starlette.responses import Response

from back.models import TablesEnum, Brigade, Department, DepartmentManager
from back.sql_server_client import db

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)


@router.get("/list")
async def get_departments():
    rows = db.select(TablesEnum.Department)
    return rows


@router.post("/add")
async def add_department(
        data: dict = Body(...)
):
    db.insert(Department(name=data['name']))

    return Response(status_code=201, content='Department created')


@router.put("/update")
async def update_department(
        data: dict = Body(...)
):
    department_id = data['department_id']
    new_name = data['name']

    db.update(Department(department_id=department_id, name=new_name))

    return Response(status_code=201, content='Department updated')


@router.delete("/delete")
async def delete_department(
        data: dict = Body(...)
):
    department_id = data['department_id']
    new_department_id = data['new_department_id']

    brigades = db.select(TablesEnum.Brigade, {'department_id': department_id})

    for brigade in brigades:
        db.update(Brigade(**{
            **brigade,
            'department_id': new_department_id
        }))

    db.delete_where(TablesEnum.DepartmentManager, {'department_id': department_id})
    db.delete(Department(department_id=department_id))

    return brigades
