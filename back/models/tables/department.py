from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Department(SQLServerTable):
	department_id: Optional[int] = None
	name: Optional[str] = None
