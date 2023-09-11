from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task4(SQLServerProcedure):
	airport_id: Optional[int] = None
	datetime_range_start: Optional[str] = None
	datetime_range_end: Optional[str] = None
