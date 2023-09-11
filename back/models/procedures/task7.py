from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task7(SQLServerProcedure):
	from_airport: Optional[int] = None
	to_airport: Optional[int] = None
