from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task3(SQLServerProcedure):
	passed: Optional[bool] = None
	year: Optional[int] = None
