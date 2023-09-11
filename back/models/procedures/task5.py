from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task5(SQLServerProcedure):
	inspection_date_range_start: Optional[str] = None
	inspection_date_range_end: Optional[str] = None
	repair_count: Optional[int] = None
