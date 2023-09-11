from fastapi import APIRouter

from back.models import TablesEnum
from back.sql_server_client import db

router = APIRouter(
    prefix="/departments",
    tags=["departments"],
)


@router.get("/list")
async def get_departments():
    rows = db.select(TablesEnum.Department)
    return rows
