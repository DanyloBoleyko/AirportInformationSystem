from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task11(SQLServerProcedure):
	flight_id: Optional[int] = None
	has_baggage: Optional[bool] = None
	gender: Optional[str] = None
