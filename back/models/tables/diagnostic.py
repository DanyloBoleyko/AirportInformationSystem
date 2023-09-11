from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Diagnostic(SQLServerTable):
	diagnostic_id: Optional[int] = None
	employee_id: Optional[int] = None
	diagnostic_date: Optional[str] = None
	diagnostic_status: Optional[str] = None
