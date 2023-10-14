from src.section1.task4 import format_staff

def test_should_accept_dict_lists_of_staff_and_dict_list_of_department_should_return_empty_list_if_either_is_blank():
    staff_list = [
        {'staff_id': 1,
        'first_name': 'Danika',
        'last_name': 'Crawley',
        'department': 'Beauty'}, 
        {'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'}]
    depart_list = []
    new_staff_lst1 = format_staff(staff_list, depart_list)
    assert new_staff_lst1  == []

    staff_list = []
    depart_list = [
        {'department_id': 1,
        'department_name':'Beauty'}, 
        {'department_id': 2,
        'department_name':'Footwear'}]
    new_staff_lst1 = format_staff(staff_list, depart_list)
    assert new_staff_lst1  == []

def test_should_accept_dict_lists_of_staff_and_dict_list_of_depart_should_return_a_list_of_lists_containing_first_name_last_name_and_the_correct_department_id():
    staff_list = [
        {'staff_id': 1,
        'first_name': 'Danika',
        'last_name': 'Crawley',
        'department': 'Beauty'}, 
        {'staff_id': 2,
        'first_name': 'Cat',
        'last_name': 'Hoang',
        'department': 'Footwear'}]
    depart_list = [
        {'department_id': 1,
        'department_name':'Beauty'}, 
        {'department_id': 2,
        'department_name':'Footwear'}]
    new_staff_lst2 = format_staff(staff_list, depart_list)
    assert new_staff_lst2  == [['Danika', 'Crawley', 1], ['Cat', 'Hoang', 2]]
    
def test_should_insert_None_for_department_id__where_a_corresponding_department_could_not_be_found_for_a_given_staff():
    staff_list = [{'staff_id': 1,
                    'first_name': 'Danika',
                    'last_name': 'Crawley',
                    'department': 'Beauty'}, 
                    {'staff_id': 2,
                    'first_name': 'Cat',
                    'last_name': 'Hoang',
                    'department': 'Footwear'}]
    depart_list = [{'department_id': 1, 'department_name':'Children'}]

    new_staff_lst3 = format_staff(staff_list, depart_list)
    assert new_staff_lst3  == [['Danika', 'Crawley', None], ['Cat', 'Hoang', None]]

def test_should_return_a_list_of_lists_and_each_list_should_have_3_elements():
    staff_list = [
            {'staff_id': 1,
            'first_name': 'Danika',
            'last_name': 'Crawley',
            'department': 'Beauty'}, 
            {'staff_id': 2,
            'first_name': 'Cat',
            'last_name': 'Hoang',
            'department': 'Footwear'}]
    depart_list = [
        {'department_id': 1,
        'department_name':'Beauty'}, 
        {'department_id': 2,
        'department_name':'Footwear'}]
    
    new_staff_lst4 = format_staff(staff_list, depart_list)

    # returned result is a list
    assert type(new_staff_lst4) == type([])

    # every element within the holding list is a list
    for staff in new_staff_lst4:
        assert type(staff) == type([])

    # each list within the holding list contains exactly 3 elements
    for staff in new_staff_lst4:
        assert len(staff) == 3
    
def test_should_not_mutate_original_list_of_dictionaries():
    staff_list = [
                {'staff_id': 1,
                'first_name': 'Danika',
                'last_name': 'Crawley',
                'department': 'Beauty'}, 
                {'staff_id': 2,
                'first_name': 'Cat',
                'last_name': 'Hoang',
                'department': 'Footwear'}]
    
    assert staff_list[0] == {'staff_id': 1,
                'first_name': 'Danika',
                'last_name': 'Crawley',
                'department': 'Beauty'}
    assert staff_list[1] == {'staff_id': 2,
                'first_name': 'Cat',
                'last_name': 'Hoang',
                'department': 'Footwear'}

    depart_list = [
            {'department_id': 1,
            'department_name':'Beauty'}, 
            {'department_id': 2,
            'department_name':'Footwear'}]
    
    assert depart_list[0] == {'department_id': 1,
            'department_name':'Beauty'}
    assert depart_list[1] == {'department_id': 2,
            'department_name':'Footwear'}
