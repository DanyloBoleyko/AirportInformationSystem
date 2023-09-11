from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task13(SQLServerProcedure):
	flight_id: Optional[int] = None
