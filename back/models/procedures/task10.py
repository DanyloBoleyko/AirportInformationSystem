from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task10(SQLServerProcedure):
	aircraft_type: Optional[int] = None
	from_airport: Optional[int] = None
	to_airport: Optional[int] = None
