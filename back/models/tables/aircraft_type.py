from typing import Optional
from back.sql_server_client.models import SQLServerTable


class AircraftType(SQLServerTable):
	aircraft_type_id: Optional[int] = None
	type: Optional[str] = None
	name: Optional[str] = None
	place_count: Optional[int] = None
