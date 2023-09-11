from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task2(SQLServerProcedure):
	department_id: Optional[int] = None
	department_name: Optional[str] = None
	flight_id: Optional[int] = None
