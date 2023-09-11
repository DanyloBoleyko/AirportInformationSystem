from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Aircraft(SQLServerTable):
	aircraft_id: Optional[int] = None
	aircraft_type_id: Optional[int] = None
	name: Optional[str] = None
	built_date: Optional[str] = None
	flight_count: Optional[int] = None
	repair_count: Optional[int] = None
