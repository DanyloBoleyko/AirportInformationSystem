from typing import Optional
from back.sql_server_client.models import SQLServerTable


class Employee(SQLServerTable):
	employee_id: Optional[int] = None
	profession_id: Optional[int] = None
	name: Optional[str] = None
	gender: Optional[str] = None
	children: Optional[int] = None
	address: Optional[str] = None
	telephone: Optional[str] = None
	birth_date: Optional[str] = None
	marital_status: Optional[str] = None
	start_working_date: Optional[str] = None
