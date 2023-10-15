from src.section1.task6 import *

# arrange
new_stock_data = [{'stock_id': 1, 'item_name': 'Louboutin Flip Flops', 'amount_in_stock':  50},
    {'stock_id': 2, 'item_name': 'Eau de Fromage', 'amount_in_stock':  20},
    {'stock_id': 3, 'item_name': 'Space Raiders', 'amount_in_stock':  50},
    {'stock_id': 4, 'item_name': 'Bags be gone', 'amount_in_stock':  10},
    {'stock_id': 5, 'item_name': 'Croc Martins', 'amount_in_stock':  80}]

new_staff_data = [{'staff_id': 1, 'first_name': 'Danika', 'last_name': 'Crawley'},
    {'staff_id': 2, 'first_name': 'Cat', 'last_name': 'Hoang'},
    {'staff_id': 3, 'first_name': 'Vincents', 'last_name': 'Guille'},
    {'staff_id': 4, 'first_name': 'Marlo', 'last_name': 'Stidworthy'},
    {'staff_id': 5, 'first_name': 'Lesli', 'last_name': 'Probet'},
    {'staff_id': 6, 'first_name': 'Sutherlan', 'last_name': 'Housbey'},
    {'staff_id': 7, 'first_name': 'Erastus', 'last_name': 'Vaines'},
    {'staff_id': 8, 'first_name': 'Phillipp', 'last_name': 'Zanini'},
    {'staff_id': 9, 'first_name': 'Kirbee', 'last_name': 'Abrahamovitz'},
    {'staff_id': 10, 'first_name': 'Danika', 'last_name': 'Archell'},
    {'staff_id': 11, 'first_name': 'Christie', 'last_name': 'Whitland'},
    {'staff_id': 12, 'first_name': 'Seline', 'last_name': 'Meekings'},
    {'staff_id': 13, 'first_name': 'Ailyn', 'last_name': 'Laxen'},
    {'staff_id': 14, 'first_name': 'Riley', 'last_name': 'Hopkynson'},
    {'staff_id': 15, 'first_name': 'Anastasie', 'last_name': 'Mordan'},
    {'staff_id': 16, 'first_name': 'Stefanie', 'last_name': 'Dartan'},
    {'staff_id': 17, 'first_name': 'Tannie', 'last_name': 'Whiteland'}]

orig_sales_data = [{'sales_code': 'guiiljnevn', 'item_name': 'Louboutin Flip Flops', 'salesperson': 'Danika Crawley', 'price':  14.95,'quantity':  2,'created_at': '2023-01-08 04:05:06'},
    {'sales_code': '48yv929f0w', 'item_name': 'Eau de Fromage', 'salesperson': 'Danika Crawley', 'price':  29.95, 'quantity': 1,'created_at': '2023-01-18 05:09:34'},
    {'sales_code': '4opsvio2to', 'item_name': 'Space Raiders', 'salesperson': 'Sutherlan Housbey', 'price':  23.47,'quantity':  26,'created_at': '2023-01-27 14:10:36'},
    {'sales_code': 'tvazcdxoup', 'item_name': 'Bags be gone', 'salesperson': 'Vincents Guille', 'price':  43.53,'quantity':  19,'created_at': '2023-01-07 09:27:43'},
    {'sales_code': '5w7nzlxgy8', 'item_name': 'Croc Martins', 'salesperson': 'Cat Hoang', 'price':  59.08,'quantity':  18,'created_at': '2023-01-03 10:34:56'}]

test_sales_item1 = orig_sales_data[0]
test_sales_item2 = orig_sales_data[1]
test_sales_item3 = orig_sales_data[2]
test_corrupted_sale_item = {'sales_code': '5w7nzlxgy89', 'item_name': '???', 'salesperson': '???', 'price':  59.08,'quantity':  18,'created_at': '2023-01-03 10:34:56'}

def test_find_stock_id_func_should_return_None_when_supplied_a_list_with_missing_key_value():
    assert find_stock_id([], test_sales_item1) == None
    assert find_stock_id([], test_corrupted_sale_item) == None

def test_find_stock_id_func_should_return_correct_stock_id():
      assert find_stock_id(new_stock_data, test_sales_item1) == 1
      assert find_stock_id(new_stock_data, test_sales_item2) == 2
      assert find_stock_id(new_stock_data, test_sales_item3) == 3

def test_find_staff_id_func_should_return_None_when_supplied_a_list_with_missing_key_value():
    assert find_staff_id([], test_sales_item3) == None
    assert find_staff_id(new_staff_data, test_corrupted_sale_item) == None

def test_find_staff_id_func_should_return_correct_staff_id():
      assert find_staff_id(new_staff_data, test_sales_item1) == 1
      assert find_staff_id(new_staff_data, test_sales_item2) == 1
      assert find_staff_id(new_staff_data, test_sales_item3) == 6

def test_format_sales_func_should_return_None_when_supplied_a_list_with_missing_key_value():
    assert format_sales([], [], [test_sales_item3]) == [[None, None, 23.47, 26, '2023-01-27 14:10:36']]
    assert format_sales(new_stock_data, new_staff_data, [test_corrupted_sale_item]) == [[None, None, 59.08, 18, '2023-01-03 10:34:56']]

def test_format_sales_func_should_return_a_correctly_formatted_list_of_lists_of_stock_id_staff_id_price_quantity_created_at():
    
    output = format_sales(new_stock_data, new_staff_data, orig_sales_data) 
    #  print(output)
    expected = [[1, 1, 14.95, 2, '2023-01-08 04:05:06'], 
                 [2, 1, 29.95, 1, '2023-01-18 05:09:34'], 
                 [3, 6, 23.47, 26, '2023-01-27 14:10:36'], 
                 [4, 3, 43.53, 19, '2023-01-07 09:27:43'], 
                 [5, 2, 59.08, 18, '2023-01-03 10:34:56']]

    assert output == expected

def test_format_sales_func_should_not_have_mutated_original_data_arguments_supplied():

    output = format_sales(new_stock_data, new_staff_data, orig_sales_data) 
    assert new_stock_data[0] == {'stock_id': 1, 'item_name': 'Louboutin Flip Flops', 'amount_in_stock':  50}
    assert new_staff_data[0] == {'staff_id': 1, 'first_name': 'Danika', 'last_name': 'Crawley'}
    assert orig_sales_data[0] == {'sales_code': 'guiiljnevn', 'item_name': 'Louboutin Flip Flops', 'salesperson': 'Danika Crawley', 'price':  14.95,'quantity':  2,'created_at': '2023-01-08 04:05:06'}
