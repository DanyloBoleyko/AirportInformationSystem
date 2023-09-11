from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Luggage(SQLServerTable):
	luggage_id: Optional[int] = None
	passenger_id: Optional[int] = None
	weight: Optional[int] = None
