from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Ticket(SQLServerTable):
	ticket_id: Optional[int] = None
	flight_id: Optional[int] = None
	created_datetime: Optional[str] = None
	passed_datetime: Optional[str] = None
	place_number: Optional[int] = None
	status: Optional[str] = None
