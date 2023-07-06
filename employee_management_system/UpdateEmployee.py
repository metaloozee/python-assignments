def update():
    try:
        id_to_modify: input("enter employee's id to modify: ")
        with open('employees.txt', '+r') as f:
            employees = f.readlines()
            flag = False

            for i, employee in enumerate(employees):
                name, id = employee.strip().split('-')
                if id == id_to_modify:
                    flag = True

                    print("\nCurrent Employee Details: \n")
                    print(f"name: {name}, id: {id}")

                    new_name = input("enter employee's new name: ")
                    new_id = input("enter employee's new id: ")

                    if new_name:
                        employees[i] = f"{new_name}-{new_id}\n"
                    else:
                        employees[i] = f"{name}-{id}\n"
                    
                    f.seek(0)
                    f.writelines(employees)
                    f.truncate()

                    print("successfully updated employee's details")
                    break

            if not flag:
                print("employee not found")
    except Exception as e:
        print("an error occurred in update.py")