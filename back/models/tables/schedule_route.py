from typing import Optional
from back.sql_server_client.models import SQLServerTable


class ScheduleRoute(SQLServerTable):
	schedule_route_id: Optional[int] = None
	schedule_id: Optional[int] = None
	to_airport_id: Optional[int] = None
	from_airport_id: Optional[int] = None
