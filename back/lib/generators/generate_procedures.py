from typing import Tuple

from back.sql_server_client import db


def generate_procedures(path: str, base_class: Tuple[str, str] = None):
    procedures = db.procedures()
    for procedure in procedures:
        imports = set()

        if base_class:
            imports.add(f'from {base_class[1]} import {base_class[0]}')
        else:
            imports.add('from pydantic import BaseModel')

        model = f"class {procedure.name}({base_class[0] if base_class else 'BaseModel'}):\n"

        datetime_imports = set()
        for parameter in procedure.parameters:
            if parameter.is_nullable:
                model += f'\t{parameter.python_name()}: Optional[{parameter.type.__name__}] = None\n'

                imports.add('from typing import Optional')
            else:
                model += f'\t{parameter.name}: {parameter.type.__name__}\n'

            if parameter.type.__name__ == 'datetime':
                datetime_imports.add('datetime')
            elif parameter.type.__name__ == 'timedelta':
                datetime_imports.add('timedelta')

        if datetime_imports:
            imports.add('from datetime import ' + ', '.join(list(datetime_imports)))

        text = ''
        text += '\n'.join(list(imports))
        text += '\n\n\n'
        text += model

        with open(f'{path}\\{procedure.python_name()}.py', 'w') as f:
            f.write(text)

    with open(f'{path}\\__init__.py', 'w') as f:
        text = 'from enum import Enum\n\n'
        for procedure in procedures:
            text += f'from .{procedure.python_name()} import {procedure.name}\n'

        text += '\n\n'

        text += 'class ProceduresEnum(str, Enum):\n'
        for procedure in procedures:
            text += f'\t{procedure.name} = "{procedure.name}"\n'

        f.write(text)


if __name__ == '__main__':
    generate_procedures(
        path='models\\procedures',
        base_class=('SQLServerProcedure', 'back.sql_server_client.models')
    )
