from enum import Enum

from .get_salary import GetSalary
from .get_total_employee_count import GetTotalEmployeeCount
from .task1 import Task1
from .task10 import Task10
from .task11 import Task11
from .task12 import Task12
from .task13 import Task13
from .task2 import Task2
from .task3 import Task3
from .task4 import Task4
from .task5 import Task5
from .task6 import Task6
from .task7 import Task7
from .task8 import Task8
from .task9 import Task9


class ProceduresEnum(str, Enum):
	GetSalary = "GetSalary"
	GetTotalEmployeeCount = "GetTotalEmployeeCount"
	Task1 = "Task1"
	Task10 = "Task10"
	Task11 = "Task11"
	Task12 = "Task12"
	Task13 = "Task13"
	Task2 = "Task2"
	Task3 = "Task3"
	Task4 = "Task4"
	Task5 = "Task5"
	Task6 = "Task6"
	Task7 = "Task7"
	Task8 = "Task8"
	Task9 = "Task9"
