from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task6(SQLServerProcedure):
	from_airport: Optional[int] = None
	to_airport: Optional[int] = None
	flight_time: Optional[str] = None
	ticket_price: Optional[int] = None
