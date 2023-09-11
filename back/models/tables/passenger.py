from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Passenger(SQLServerTable):
	passenger_id: Optional[int] = None
	ticket_id: Optional[int] = None
	name: Optional[str] = None
	age: Optional[int] = None
	gender: Optional[str] = None
	passport_number: Optional[str] = None
	international_passport_number: Optional[str] = None
	customs_control_status: Optional[str] = None
