def format_departments(dept_dict):
    if dept_dict == [{}]:
        return [[]]

    dept_list = []
    for i in range(len(dept_dict)):
        staff = dept_dict[i]
        dept_name = []
        dept_name.append(staff['department'])
        # print(dept_name)
        dept_list.append(dept_name)

    return dept_list


print(format_departments([{
    'staff_id': 1,
    'first_name': 'Danika',
    'last_name': 'Crawley',
    'department': 'Beauty'}]))
