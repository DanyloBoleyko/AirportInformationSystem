from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Body
from starlette.responses import Response

from back.models import TablesEnum, Task6, Passenger, Ticket
from back.sql_server_client import db

router = APIRouter(
    prefix="/tickets",
    tags=["tickets"],
)


@router.get("/list")
async def get_tickets(
        ticket_id: Optional[int] = None,
        flight_id: Optional[int] = None
):
    params = {}
    if flight_id:
        params['flight_id'] = flight_id
    if ticket_id:
        params['ticket_id'] = ticket_id
    return db.select(TablesEnum.Ticket, params)


@router.post("/buy")
async def add_employee(
        data: dict = Body(...)
):
    ticket = Ticket(
        flight_id=data['flight_id'],
        created_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        passed_datetime=None,
        place_number=data['place'],
        status='Куплено',
    )

    db.insert(ticket)

    tickets = db.select(TablesEnum.Ticket, {'flight_id': data['flight_id'], 'place_number': data['place']})

    passenger = Passenger(
        ticket_id=tickets[0]['ticket_id'],
        name=data['name'],
        age=data['age'],
        gender=data['gender'],
        passport_number=data['passport'],
    )

    db.insert(passenger)

    return Response(status_code=201, content='Employee created')
