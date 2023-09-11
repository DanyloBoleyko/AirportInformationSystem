from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Inspection(SQLServerTable):
	inspection_id: Optional[int] = None
	brigade_id: Optional[int] = None
	aircraft_id: Optional[int] = None
	inspection_datetime: Optional[str] = None
	status: Optional[str] = None
	result: Optional[str] = None
