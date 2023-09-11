from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Schedule(SQLServerTable):
	schedule_id: Optional[int] = None
	departure_days: Optional[int] = None
	estimated_flight_time: Optional[str] = None
	ticket_price: Optional[int] = None
	ticket_price_discounted: Optional[int] = None
