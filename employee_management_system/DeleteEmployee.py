def delete():
    try:
        id_to_delete = input("enter employee's id: ")
        with open('employees.txt', 'r') as f:
            employees = f.readlines()
        with open('employees.txt', 'w') as f:
            flag = False
            for employee in employees:
                name, id = employee.strip().split('-')
                if id != id_to_delete:
                    f.write(employee)
                else:
                    flag = True
            
            if flag:
                print('successfully deleted the employee')
            else:
                print('employee not found')
    except Exception as e:
        print('an error occurred in delete.py')