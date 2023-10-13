def format_stock(stock_dict):

    stock_list = []
    for i in range(len(stock_dict)):
        item = stock_dict[i]
        stock_item = []
        stock_item.append(item['item_name'])
        stock_item.append(item['amount_in_stock'])
        print(stock_item)
        stock_list.append(stock_item)

    return stock_list

# print(format_stock([
#     {
#         'item_name': 'Louboutin Flip Flops',
#         'features': ['Designer', 'Faux-Faux-Leather'],
#         'department': 'Footwear',
#         'amount_in_stock': 5
#     }]))
