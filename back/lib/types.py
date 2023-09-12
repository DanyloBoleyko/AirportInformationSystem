from datetime import datetime, timedelta
from typing import Optional


def sql_type_to_python_type(sql_type: str) -> type:
    if sql_type in ['int', 'int identity', 'decimal', 'numeric', 'smallint', 'tinyint', 'bigint']:
        return int
    elif sql_type in ['nvarchar', 'varchar', 'char', 'text']:
        return str
    elif sql_type in ['bit']:
        return bool
    elif sql_type in ['datetime', 'date']:
        # return datetime
        return str
    elif sql_type in ['time']:
        # return timedelta
        return str
    elif sql_type in ['float']:
        return float
    else:
        raise Exception(f'Unknown type {sql_type}')


def python_value_to_sql_value(value, sql_type: Optional[str]) -> str:
    if value is None:
        return 'NULL'
    elif isinstance(value, int):
        return str(value)
    elif isinstance(value, str):
        if sql_type == 'date' or sql_type == 'datetime' or sql_type == 'time':
            return f"'{value}'"
        return f"N'{value}'"
    elif isinstance(value, bool):
        return '1' if value else '0'
    elif isinstance(value, datetime):
        if sql_type == 'date':
            return f"'{value.strftime('%Y-%m-%d')}'"
        elif sql_type == 'datetime':
            return f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"
        else:
            return f"'{value.strftime('%Y-%m-%d %H:%M:%S')}'"
    elif isinstance(value, timedelta):
        if sql_type == 'time':
            return f"'{value}'"
        else:
            return f"'{value}'"
    elif isinstance(value, float):
        return str(value)
    else:
        raise Exception(f'Unknown type {type(value)}')
