from typing import Optional

from fastapi import APIRouter

from back.models import TablesEnum
from back.sql_server_client import db

router = APIRouter(
    prefix="/airports",
    tags=["airports"],
)


@router.get("/list")
async def get_airports(
        airport_id: Optional[int] = None
):
    params = {}
    if airport_id:
        params['airport_id'] = airport_id
    return db.select(TablesEnum.Airport, params)

