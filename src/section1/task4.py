def format_staff(staff_dict, dept_dict):
    
    new_staff_list = []
    if not staff_dict or not dept_dict:
        return new_staff_list
    
    # fill list of list with fore_name, last_name and department name 
    # before replacing dept name with dept id
    new_staff_list = [[staff['first_name'], staff['last_name'], staff['department']] 
                      for staff in staff_dict]
    
    # replace department name by department id
    for i in range(len(new_staff_list)):
        depart_name = new_staff_list[i][2] 

        # use list comprehension to define the mapping function
        get_dept_id = lambda name, dept_dict: ([department['department_id'] 
                                                for department in dept_dict 
                                                if name in department.values()])
        
        # The lambda function returns a single element list holding department id
        dept_id = get_dept_id(depart_name, dept_dict)

        # now replace dept name with dept id
        new_staff_list[i][2] = dept_id[0] if dept_id else None

    return new_staff_list

