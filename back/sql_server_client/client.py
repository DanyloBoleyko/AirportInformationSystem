from typing import List, Type

import pyodbc
from decimal import Decimal

from back.lib.types import sql_type_to_python_type, python_value_to_sql_value
from back.lib.writing import camel_case_to_python_case, python_case_to_camel_case
from back.sql_server_client.models import SQLTable, SQLColumn, SQLProcedure, SQLParameter, SQLServerTable, \
    SQLServerProcedure


class SQLServerClient:
    def __init__(self):
        self.connection = pyodbc.connect(
            driver='{ODBC Driver 17 for SQL Server}',
            server='(local)',
            database='AirportInformationSystem',
            trusted_connection='yes',
            timeout=10
        )

    def select(self, table: str, params: dict = None, join: dict = None) -> List[dict]:
        cursor = self.connection.cursor()
        query_from = f'{table} {table.lower()}'
        query_select = ['*']
        table_names = set()
        table_names.add(table.lower())

        if join:
            query_select = []

            for join_table, join_key in join.items():
                table_names.add(join_table.lower())
                origin_table = table

                if isinstance(join_key, str):
                    join_key = python_case_to_camel_case(join_key, True)
                elif isinstance(join_key, tuple):
                    origin_table = join_key[0]
                    join_key = python_case_to_camel_case(join_key[1], True)

                query_from += f' JOIN {join_table} {join_table.lower()} ON {origin_table}.{join_key} = {join_table}.{join_key}'

                cols = self.columns(join_table)
                for col in cols:
                    query_select.append(f'{join_table.lower()}.{col.name} as {join_table}{col.name}')

            cols = self.columns(table)
            for col in cols:
                query_select.append(f'{table.lower()}.{col.name} as {col.name}')

        query = f'SELECT {", ".join(query_select)} FROM {query_from}'

        items = {}
        if params:
            columns = self.columns(table)
            for col in columns:
                col_name = col.python_name()
                if col_name in params:
                    items[col.name] = params[col_name]

            query += ' WHERE ' + ' AND '.join([f'{key} = ?' for key in items.keys()])

        result = cursor.execute(query, list(items.values()))
        rows = result.fetchall()
        cursor.close()
        return self.parse_rows(rows)

    def insert(self, data: SQLServerTable):
        cursor = self.connection.cursor()
        name = data.__class__.__name__
        columns = list(filter(lambda x: not x.is_identity, self.columns(name)))
        values = [getattr(data, col.python_name()) for col in columns]
        cursor.execute(
            f'INSERT INTO {name}({", ".join([n.name for n in columns])}) VALUES '
            f'({", ".join([python_value_to_sql_value(v, c.sql_type) for v, c in zip(values, columns)])})',
        )
        cursor.commit()
        cursor.close()

    def insert_many(self, data: List[SQLServerTable]):
        cursor = self.connection.cursor()
        for table in data:
            name = table.__class__.__name__
            columns = list(filter(lambda x: not x.is_identity, self.columns(name)))
            values = [getattr(table, col.python_name()) for col in columns]
            cursor.execute(
                f'INSERT INTO {name}({", ".join([n.name for n in columns])}) VALUES '
                f'({", ".join([python_value_to_sql_value(v, c.sql_type) for v, c in zip(values, columns)])})',
            )
        cursor.commit()
        cursor.close()

    def update(self, data: SQLServerTable):
        cursor = self.connection.cursor()
        name = data.__class__.__name__
        primary_key = next(filter(lambda x: x.is_identity, self.columns(name)))
        columns = list(filter(lambda x: not x.is_identity, self.columns(name)))
        values = [getattr(data, col.python_name()) for col in columns]
        cursor.execute(
            f'UPDATE {name} SET {", ".join([n.name + " = ?" for n in columns])} '
            f'WHERE {primary_key.name} = ?',
            values + [getattr(data, primary_key.python_name())]
        )
        cursor.commit()
        cursor.close()

    def delete(self, data: SQLServerTable):
        cursor = self.connection.cursor()
        name = data.__class__.__name__
        primary_key = next(filter(lambda x: x.is_identity, self.columns(name)))
        cursor.execute(
            f'DELETE FROM {name} WHERE {primary_key.name} = ?',
            [getattr(data, primary_key.python_name())]
        )
        cursor.commit()
        cursor.close()

    def delete_where(self, table: str, params: dict):
        cursor = self.connection.cursor()
        query = f'DELETE FROM {table}'

        items = {}
        columns = self.columns(table)
        for col in columns:
            col_name = col.python_name()
            if col_name in params:
                items[col.name] = params[col_name]

        query += ' WHERE ' + ' AND '.join([f'{key} = ?' for key in items.keys()])

        cursor.execute(query, list(items.values()))

        cursor.commit()
        cursor.close()

    def procedure(self, data: SQLServerProcedure) -> List[dict]:
        cursor = self.connection.cursor()
        name = data.__class__.__name__
        params = self.procedure_parameters(name)
        values = [getattr(data, param.python_name()) for param in params]
        items = list(zip(params, values))
        query = f'EXEC {name} {", ".join([p.name + " = ?" for p, v in items if v is not None])}'
        result = cursor.execute(
            query, [python_value_to_sql_value(v, p.sql_type) for p, v in items if v is not None]
        )
        rows = result.fetchall()
        result.close()
        return self.parse_rows(rows)

    def tables(self) -> List[SQLTable]:
        cursor = self.connection.cursor()
        result = cursor.tables()
        if not result:
            return []
        tables = result.fetchall()
        cursor.close()
        tables = list(filter(lambda x: x[3] == 'TABLE' and x[1] == 'dbo', tables))
        return [
            SQLTable(
                database=table[0],
                name=table[2],
                columns=self.columns(table[2])
            )
            for table in tables
        ]

    def columns(self, table: str) -> List[SQLColumn]:
        cursor = self.connection.cursor()
        result = cursor.columns(table=table)
        if not result:
            return []
        columns = result.fetchall()
        cursor.close()
        return [
            SQLColumn(
                name=column[3],
                sql_type=column[5],
                type=sql_type_to_python_type(column[5]),
                is_nullable=column[10] == 1,
                is_identity=column[21] == 1,
            )
            for column in columns
        ]

    def procedures(self):
        cursor = self.connection.cursor()
        result = cursor.procedures()
        if not result:
            return []
        procedures = result.fetchall()
        cursor.close()
        procedures = list(filter(lambda x: x[1] == 'dbo', procedures))
        return [
            SQLProcedure(
                name=procedure[2].split(';')[0],
                parameters=self.procedure_parameters(procedure[2])
            )
            for procedure in procedures
        ]

    def procedure_parameters(self, procedure: str):
        cursor = self.connection.cursor()
        result = cursor.procedureColumns(procedure=procedure)
        if not result:
            return []
        parameters = result.fetchall()
        cursor.close()
        parameters = list(filter(lambda x: x[3] != '@RETURN_VALUE', parameters))
        return [
            SQLParameter(
                name=parameter[3],
                sql_type=parameter[6],
                type=sql_type_to_python_type(parameter[6]),
                is_nullable=parameter[11] == 1
            )
            for parameter in parameters
        ]

    @staticmethod
    def parse_rows(rows: List[pyodbc.Row]):
        result = []
        for row in rows:
            obj = {}
            columns = [
                camel_case_to_python_case(column[0])
                for column in row.cursor_description
            ]
            for name, val in zip(columns, row):
                if isinstance(val, Decimal):
                    val = int(val)
                obj[name] = val

            result.append(obj)
        return result


db = SQLServerClient()
