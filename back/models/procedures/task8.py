from back.sql_server_client.models import SQLServerProcedure
from typing import Optional


class Task8(SQLServerProcedure):
	late_reason: Optional[str] = None
