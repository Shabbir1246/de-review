from src.section1.task3 import format_features

def test_should_take_a_list_of_dicts_and_return_an_empty_list_if_no_items_in_dict():
    output1 = format_features([])
    print(output1)
    assert output1  == []

def test_should_return_an_empty_entry_in_the_list_if_features_key_was_not_found():
    output1 = format_features(
        [{'item_name': 'Louboutin Flip Flops',
        'department': 'Footwear',
        'amount_in_stock': 5}])
    assert output1  == []

def test_should_take_a_list_of_dicts_and_return_a_list_of_lists_containing_feature():
    output2 = format_features([
    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }])
    assert output2 ==  [['Designer']]

    output3 = format_features([
    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }])
    assert output3 ==  [['Designer'], ['Faux-Faux-Leather']]

def test_should_take_a_list_of_dicts_and_return_a_list_of_lists_each_containing_unique_features():
    output4 = format_features([
    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }, {
        'item_name': 'Eau de Fromage',
        'features': ['Fragrance', 'Designer'],
        'department': 'Beauty',
        'amount_in_stock': 10
    }])

    # returned result is a list
    assert type(output4) == type([])
    # every element within the holding list is a list
    for feature in output4:
        assert type(feature) == type([])

    # each list within the holding list contains a single feature only
    for feature in output4:
        assert len(feature) == 1
    
    # list of list is made up of unique features from each stock item features
    assert output4 ==  [['Faux-Faux-Leather'], ['Fragrance'], ['Designer']]



