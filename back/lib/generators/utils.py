def generate_pydantic_model(class_name: str, fields: list):
    result = f'class {class_name}(SQLServerTable):\n'
    imports = []

    for field in fields:
        if field.get('is_nullable'):
            result += f'\t{field.get("name")}: Optional[{field.get("type")}] = None\n'
            imports.append('from typing import Optional')
        else:
            result += f'\t{field.get("name")}: {field.get("type")}\n'

        if field.get('type') == 'datetime':
            imports.append('from datetime import datetime')
        elif field.get('type') == 'timedelta':
            imports.append('from datetime import timedelta')

    return result, imports
