from typing import Optional
from back.sql_server_client.models import SQLServerTable


class FlightRoute(SQLServerTable):
	flight_route_id: Optional[int] = None
	flight_id: Optional[int] = None
	to_airport_id: Optional[int] = None
	from_airport_id: Optional[int] = None
	departure_time: Optional[str] = None
	arrival_time: Optional[str] = None
