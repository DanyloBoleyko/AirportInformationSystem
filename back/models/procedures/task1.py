from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task1(SQLServerProcedure):
	department_id: Optional[int] = None
