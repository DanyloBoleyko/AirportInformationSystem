from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Brigade(SQLServerTable):
	brigade_id: Optional[int] = None
	department_id: Optional[int] = None
	name: Optional[str] = None
