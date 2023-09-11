from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body
from starlette.responses import Response

from back.models import Employee, Task1, Task2, Task3, Profession, TablesEnum
from back.sql_server_client.client import db

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
)


@router.get("/list")
async def get_employees(
        department_id: Optional[int] = None
):
    """
    Одержати список і загальну кількість всіх робітників аеропорту, керівників відділів, робітників зазначеного
    відділу, за стажем роботи в аеропорту, статевою ознакою, віком, ознакою наявності та кількості дітей, за розміром
    заробітної платні.
    """
    rows = db.procedure(Task1(
        department_id=department_id
    ))
    return rows


@router.post("/add")
async def add_employee(
        data: dict = Body(...)
):
    profession = db.select(TablesEnum.Profession, {'name': data['profession']})
    if not profession:
        return Response(status_code=400, content='Profession not found')

    brigade = db.select(TablesEnum.Profession, {'name': data['brigade']})
    if not profession:
        return Response(status_code=400, content='Brigade not found')

    employee = Employee(**{
        **data,
        'profession_id': profession[0]['profession_id'],
        'birth_date': data.get('start_working_date', datetime.now().strftime('%Y-%m-%d')),
        'start_working_date': data.get('start_working_date', datetime.now().strftime('%Y-%m-%d'))
    })

    db.insert(employee)

    return Response(status_code=201, content='Employee created')


@router.get("/brigade")
async def get_employees_by_brigade(
        department_id: Optional[int] = None,
        department_name: Optional[str] = None,
        flight_id: Optional[int] = None
):
    """
    Одержати перелік і загальну кількість робітників в бригаді, по усіх відділах, у зазначеному відділі,
    які обслуговують конкретний рейс, за віком, за сумарною (середньою) зарплатнею в бригаді
    """
    rows = db.procedure(Task2(
        department_id=department_id,
        department_name=department_name,
        flight_id=flight_id
    ))
    return rows


@router.get("/pilots")
async def get_pilots(
        diagnostic_passed: Optional[bool] = True,
        diagnostic_year: Optional[int] = None
):
    """
    Одержати перелік і загальну кількість пілотів, які пройшли медогляд або не пройшли його в зазначений рік,
    за статевою ознакою, за віком, за розміром заробітної платні
    """
    rows = db.procedure(Task3(
        passed=diagnostic_passed,
        year=diagnostic_year
    ))
    return rows
