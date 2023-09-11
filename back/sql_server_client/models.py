from typing import List

from pydantic import BaseModel

from back.lib.writing import camel_case_to_python_case


class SQLObject(BaseModel):
    name: str

    def python_name(self) -> str:
        return camel_case_to_python_case(self.name)


class SQLParameter(SQLObject):
    sql_type: str
    type: type
    is_nullable: bool

    def python_name(self) -> str:
        return camel_case_to_python_case(self.name.replace('@', ''))


class SQLColumn(SQLObject):
    sql_type: str
    type: type
    is_nullable: bool
    is_identity: bool


class SQLTable(SQLObject):
    database: str
    columns: List[SQLColumn]


class SQLProcedure(SQLObject):
    parameters: List[SQLParameter]


class SQLServerTable(BaseModel):
    pass


class SQLServerProcedure(BaseModel):
    pass
