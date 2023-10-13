from src.section1.task2 import format_stock


def test_should_take_a_list_of_dicts_and_return_a_list_of_lists():
    output1 = format_stock([])
    assert output1  == []

    output2 = format_stock([
    {
        'item_name': 'Louboutin Flip Flops',
        'features': ['Designer', 'Faux-Faux-Leather'],
        'department': 'Footwear',
        'amount_in_stock': 5
    }])
    assert output2 ==  [['Louboutin Flip Flops', 5]]

    output3 = format_stock([
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
    }
])
    assert output3 == [['Louboutin Flip Flops',5], ['Eau de Fromage', 10]]