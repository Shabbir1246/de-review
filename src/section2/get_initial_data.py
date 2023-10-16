from pg8000.native import Connection, InterfaceError, DatabaseError
from db.coonect_org import *

def get_staff_data():

    try:
        db = get_conn()
    except Exception:
        return 'Error connecting database'
    
    query = (f'SELECT * FROM staff')
    staff_list = db.run(query)

    staff_dict_list = []
    for staff_id, first_name, last_name, department in staff_list:
        staff_dict = {}
        staff_dict['staff_id'] = staff_id
        staff_dict['first_name'] = first_name
        staff_dict['last_name'] = last_name
        staff_dict['department'] = department
        
        staff_dict_list.append(staff_dict)

    return staff_dict_list

# print(get_staff_data())

def get_item_data():
    try:
        db = get_conn()
    except Exception:
        return 'Error connecting database'
    
    query = (f'SELECT * FROM items')
    item_list = db.run(query)

    item_dict_list = []
    for item_name, features, department, amount_in_stock in item_list:
        item_dict = {}
        item_dict['item_name'] = item_name
        item_dict['features'] = features
        item_dict['department'] = department
        item_dict['amount_in_stock'] = amount_in_stock
        
        item_dict_list.append(item_dict)

    return item_dict_list

# print(get_item_data())

def get_sales_data():
    try:
        db = get_conn()
    except Exception:
        return 'Error connecting database'
    
    query = (f'SELECT * FROM sales')
    sales_list = db.run(query)

    sales_dict_list = []
    for sale_code, item_name, salesperson, price, quantity, created_at in sales_list:
        sales_dict = {}
        sales_dict['sale_code'] = sale_code
        sales_dict['item_name'] = item_name
        sales_dict['salesperson'] = salesperson
        sales_dict['price'] = float(price)
        sales_dict['quantity'] = quantity
        sales_dict['created_at'] = format(created_at)

        sales_dict_list.append(sales_dict)

    return sales_dict_list

# print(get_sales_data())