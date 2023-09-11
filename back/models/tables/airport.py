from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Airport(SQLServerTable):
	airport_id: Optional[int] = None
	name: Optional[str] = None
	country: Optional[str] = None
	city: Optional[str] = None
