from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Profession(SQLServerTable):
	profession_id: Optional[int] = None
	name: Optional[str] = None
	salary: Optional[int] = None
