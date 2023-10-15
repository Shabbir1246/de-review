def format_sales(stock_new, staff_new, sales_orig):
    formatted_sales = []
    formatted_sales = [[find_stock_id(stock_new, sales_item), 
                        find_staff_id(staff_new, sales_item),
                        sales_item['price'],
                        sales_item['quantity'],
                        sales_item['created_at']                        ]
                       for sales_item in sales_orig]
    return formatted_sales

    
# given a single original stock dict, 
# return corresponding stock_id in new stock data 
def find_stock_id(stock_new, sales_item):
    if not stock_new:
        return None
    stock_id = [stock['stock_id'] for stock in stock_new 
                if stock['item_name'] == sales_item['item_name']]
    return stock_id[0] if stock_id else None

# given a single original staff dict containing salesperson, 
# return corresponding staff_id in new staff data 
def find_staff_id(staff_new, sales_item):
    if not staff_new:
        return None
    staff_id = []
    salesperson = sales_item['salesperson'].rsplit()
    staff_id = [staff['staff_id'] for staff in staff_new 
                if staff['first_name'] == salesperson[0] and
                    staff['last_name'] == salesperson[1]]
    return staff_id[0] if staff_id else None
    