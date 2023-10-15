from src.section1.task5 import *

# arrange
new_stock_data = [{'stock_id': 1, 'item_name': 'Louboutin Flip Flops', 'amount_in_stock':5}, 
                    {'stock_id': 2, 'item_name': 'Eau de Fromage', 'amount_in_stock': 10}]
new_feature_data = [{'feature_id':1, 'feature_name':'Designer'},
                    {'feature_id':2, 'feature_name':'Faux-Faux-Leather'}]
original_stock_data = [{'item_name': 'Louboutin Flip Flops', 'features': ['Designer', 'Faux-Faux-Leather'], 
                        'department': 'Footwear', 'amount_in_stock': 5}, 
                        {'item_name': 'Eau de Fromage', 'features': ['Designer'],
                        'department': 'Beauty', 'amount_in_stock': 10}]
def test_should_return_empty_list_if_either_new_stock_new_features_or_original_stock_lists_are_empty():
    # act
    stock_feature = format_stock_feature(new_stock_data, [], original_stock_data )

    # assert
    assert stock_feature == []

def test_should_return_a_list_of_lists_comprising_of_stock_id_and_feature_id():
    # act
    stock_feature = format_stock_feature(new_stock_data, new_feature_data, original_stock_data )

    # assert
    assert stock_feature == [[1, 1], [1, 2], [2, 1]]

def test_should_disregard_missing_items_from_new_stock_data():
    # act
    # stock item 'Eau de Fromage' missing from new_stock_data
    incomplete_stock_data = [{'stock_id': 1, 'item_name': 'Louboutin Flip Flops', 'amount_in_stock':5}]
    stock_feature = format_stock_feature(incomplete_stock_data, new_feature_data, original_stock_data )

    # assert
    assert stock_feature == [[1, 1], [1, 2]]

def test_should_disregard_missing_features_from_new_feature_data():
    # act
    # feature 'Designer' missing from new_feature_data
    incomplete_feature_data = [{'feature_id':2, 'feature_name':'Faux-Faux-Leather'}]
    stock_feature = format_stock_feature(new_stock_data, incomplete_feature_data, original_stock_data )

    # assert
    assert stock_feature == [[1, 2]]


