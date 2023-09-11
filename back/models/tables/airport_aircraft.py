from typing import Optional
from back.sql_server_client.models import SQLServerTable


class AirportAircraft(SQLServerTable):
	airport_aircraft_id: Optional[int] = None
	aircraft_id: Optional[int] = None
	airport_id: Optional[int] = None
	creation_time: Optional[str] = None
