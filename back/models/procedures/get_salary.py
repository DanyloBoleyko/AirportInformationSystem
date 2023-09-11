from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class GetSalary(SQLServerProcedure):
	profession_salary: Optional[int] = None
	children_count: Optional[int] = None
