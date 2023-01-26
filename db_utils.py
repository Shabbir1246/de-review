import pg8000.native as pg

# change the variable below to your psql username. Don't forget to add your password if needed.
DB_USERNAME = "verity"
DB_NAME = "nc_sells_fridges_draft"
conn = pg.Connection(DB_USERNAME,database=DB_NAME)

def get_items():
    query = 'SELECT * FROM items'
    rows = conn.run(query)
    column_names = [col['name']for col in conn.columns]

    return rows, column_names

def get_staff():
    query = 'SELECT * FROM staff'
    rows = conn.run(query)
    column_names = [col['name']for col in conn.columns]
    return rows, column_names

def get_sales():
    query = 'SELECT * FROM sales'
    rows = conn.run(query)
    column_names = [col['name']for col in conn.columns]
    return rows, column_names

