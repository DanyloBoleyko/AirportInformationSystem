from typing import Tuple, Optional

from back.sql_server_client import db


def generate_tables(path: str, base_class: Optional[Tuple[str, str]] = None):
    tables = db.tables()
    for table in tables:
        imports = set()

        if base_class:
            imports.add(f'from {base_class[1]} import {base_class[0]}')
        else:
            imports.add('from pydantic import BaseModel')

        model = f"class {table.name}({base_class[0] if base_class else 'BaseModel'}):\n"

        datetime_imports = set()
        for column in table.columns:
            if column.is_nullable or column.is_identity:
                model += f'\t{column.python_name()}: Optional[{column.type.__name__}] = None\n'

                imports.add('from typing import Optional')
            else:
                model += f'\t{column.python_name()}: {column.type.__name__}\n'

            if column.type.__name__ == 'datetime':
                datetime_imports.add('datetime')
            elif column.type.__name__ == 'timedelta':
                datetime_imports.add('timedelta')

        if datetime_imports:
            imports.add('from datetime import ' + ', '.join(list(datetime_imports)))

        text = ''
        text += '\n'.join(list(imports))
        text += '\n\n\n'
        text += model

        with open(f'{path}\\{table.python_name()}.py', 'w') as f:
            f.write(text)

    with open(f'{path}\\__init__.py', 'w') as f:
        text = 'from enum import Enum\n\n'
        for table in tables:
            text += f'from .{table.python_name()} import {table.name}\n'

        text += '\n\n'

        text += 'class TablesEnum(str, Enum):\n'
        for table in tables:
            text += f'\t{table.name} = "{table.name}"\n'

        f.write(text)


if __name__ == '__main__':
    generate_tables(
        path='models\\tables',
        base_class=('SQLServerTable', 'back.sql_server_client.models')
    )
