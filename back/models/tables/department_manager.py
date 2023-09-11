from typing import Optional
from back.sql_server_client.models import SQLServerTable


class DepartmentManager(SQLServerTable):
	department_manager_id: Optional[int] = None
	employee_id: Optional[int] = None
	department_id: Optional[int] = None
	start_datetime: Optional[str] = None
	end_datetime: Optional[str] = None
