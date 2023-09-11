from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class GetTotalEmployeeCount(SQLServerProcedure):
	department_id: Optional[int] = None
	department_name: Optional[str] = None
	brigade_id: Optional[int] = None
	brigade_name: Optional[str] = None
