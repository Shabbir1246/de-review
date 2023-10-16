from pg8000.native import Connection, InterfaceError, DatabaseError

def get_conn():
    return Connection(
        user = 'a',
        host = 'localhost',
        database = 'nc_sells_fridges_og',
        password = '1234')


