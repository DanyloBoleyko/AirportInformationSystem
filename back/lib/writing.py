def python_case_to_camel_case(name: str, capitalize: bool = False) -> str:
    parts = name.split('_')
    if capitalize:
        parts[0] = parts[0].capitalize()
    return ''.join(
        part.capitalize() if len(part) > 2 else part.upper()
        for part in parts
    )


def camel_case_to_python_case(name: str) -> str:
    parts = []
    name = name.replace('ID', 'Id')
    for part in name:
        if part.isupper() and parts:
            parts.append('_')
        parts.append(part.lower())
    return ''.join(parts)
