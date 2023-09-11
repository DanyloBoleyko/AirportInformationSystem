from fastapi import APIRouter

from back.models import TablesEnum
from back.sql_server_client import db

router = APIRouter(
    prefix="/professions",
    tags=["professions"],
)


@router.get("/list")
async def get_professions():
    return db.select(TablesEnum.Profession)

