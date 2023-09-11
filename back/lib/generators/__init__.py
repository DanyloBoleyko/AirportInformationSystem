from back.lib.generators.generate_procedures import generate_procedures
from back.lib.generators.generate_tables import generate_tables

if __name__ == '__main__':
    generate_tables(
        path='models\\tables',
        base_class=('SQLServerTable', 'back.sql_server_client.models')
    )
    generate_procedures(
        path='models\\procedures',
        base_class=('SQLServerProcedure', 'back.sql_server_client.models')
    )
