from src.section1.task1 import format_departments


def test_should_take_a_list_of_dicts_and_return_a_list_of_lists():
    output1 = format_departments([{}])
    assert output1  == [[]]
    
def test_should_take_a_list_of_dicts_and_return_a_list_of_lists_of_departments():    
    output2 = format_departments([{
        'staff_id': 1,
        'first_name': 'Danika',
        'last_name': 'Crawley',
        'department': 'Beauty'}])
    assert output2 == [['Beauty']]
    
    output3 = format_departments([
    {
        'staff_id': 1,
        'first_name': 'Danika',
        'last_name': 'Crawley',
        'department': 'Beauty'
    },
    {
        'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'
    }
])
    assert output3 == [['Beauty'], ['Footwear']]