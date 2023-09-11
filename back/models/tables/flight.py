from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Flight(SQLServerTable):
	flight_id: Optional[int] = None
	aircraft_id: Optional[int] = None
	schedule_id: Optional[int] = None
	departure_datetime: Optional[str] = None
	departure_late_reason: Optional[str] = None
	arrival_datetime: Optional[str] = None
	arrival_late_reason: Optional[str] = None
	status: Optional[str] = None
