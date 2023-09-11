from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task12(SQLServerProcedure):
	flight_id: Optional[int] = None
