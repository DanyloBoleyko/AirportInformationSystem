from enum import Enum

from .aircraft import Aircraft
from .aircraft_brigade import AircraftBrigade
from .aircraft_type import AircraftType
from .airport import Airport
from .airport_aircraft import AirportAircraft
from .brigade import Brigade
from .department import Department
from .department_manager import DepartmentManager
from .diagnostic import Diagnostic
from .employee import Employee
from .employee_brigade import EmployeeBrigade
from .flight import Flight
from .flight_route import FlightRoute
from .inspection import Inspection
from .luggage import Luggage
from .passenger import Passenger
from .profession import Profession
from .schedule import Schedule
from .schedule_route import ScheduleRoute
from .ticket import Ticket


class TablesEnum(str, Enum):
	Aircraft = "Aircraft"
	AircraftBrigade = "AircraftBrigade"
	AircraftType = "AircraftType"
	Airport = "Airport"
	AirportAircraft = "AirportAircraft"
	Brigade = "Brigade"
	Department = "Department"
	DepartmentManager = "DepartmentManager"
	Diagnostic = "Diagnostic"
	Employee = "Employee"
	EmployeeBrigade = "EmployeeBrigade"
	Flight = "Flight"
	FlightRoute = "FlightRoute"
	Inspection = "Inspection"
	Luggage = "Luggage"
	Passenger = "Passenger"
	Profession = "Profession"
	Schedule = "Schedule"
	ScheduleRoute = "ScheduleRoute"
	Ticket = "Ticket"
