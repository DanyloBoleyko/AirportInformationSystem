from typing import Optional
from back.sql_server_client.models import SQLServerTable


class AircraftBrigade(SQLServerTable):
	aircraft_brigade_id: Optional[int] = None
	brigade_id: Optional[int] = None
	aircraft_id: Optional[int] = None
	start_datetime: Optional[str] = None
	end_datetime: Optional[str] = None
