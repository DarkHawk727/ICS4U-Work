import numpy as np
from tabulate import tabulate

datatype = np.dtype(
    [
        ("Employee#", str, 4),
        ("Name", str, 16),
        ("Marital Status", str, 1),
        ("Age", np.int32),
        ("Salary", np.int32),
    ]
)


def load_file(filepath):
    with open(filepath, "r") as data:
        table = np.loadtxt(data, dtype=datatype, skiprows=1)
    return table


def save_file(table, filepath):
	with open(filepath, "w") as data:
		data.write("Employee#\tName\tMarital Status\tAge\tSalary\n")
		np.savetxt(data, table, fmt="%s")


def add_employee(table):
    temp_row = np.empty((1,), dtype=datatype)

    employee_number = str(input("Please enter the employee number: "))
    name = str(input("Please enter the name ([First Initial].[Last Name]: "))
    maritial_status = str(input("Please enter the employee's maritial status (M or S): ")).upper()
    age = int(input("Please enter the age of the employee: "))
    salary = int(input("Please enter the employee's salary: "))

    temp_row["Employee#"] = employee_number
    temp_row["Name"] = name
    temp_row["Marital Status"] = maritial_status
    temp_row["Age"] = age
    temp_row["Salary"] = salary

    return np.append(table, temp_row)


def delete_employee(table, index):
	if index > len(table):
		print("Index out of range")
		return table
	else:
		table = np.delete(table, index)
		return table


def modify_table(table):
    display_all(table)
    index = int(input("Please select the index of the employee you would like to modify: "))
    new_employee_num = str(input("Please enter the new employee number: "))
    # Check if the employee number is unique
    if new_employee_num in table["Employee#"]:
        print("Employee number already exists!")
        return table
    else:
        table["Employee#"][index] = new_employee_num
    table[index]["Name"] = str(input("Please enter the new name: "))
    table[index]["Marital Status"] = str(input("Please enter the new maritial status: "))
    table[index]["Age"] = int(input("Please enter the new age: "))
    table[index]["Salary"] = int(input("Please enter the new salary: "))
    return table


def display_all(table):
    headers = ["Employee Number", "Name", "Marital Status", "Age", "Salary"]
    pretty_table = tabulate(table, headers, tablefmt="fancy_grid", numalign="center")
    print(pretty_table)


print("Welcome to the Employee Database")
print("Please select an option from the menu below:")
print("1. Load File")
print("2. Save File")
print("3. Add Employee")
print("4. Delete Employee")
print("5. Modify Employee")
print("6. Display All")
print("7. Exit")

choice = 0
while choice != 7:
    choice = int(input("Please enter a choice (1-7): "))
    if choice == 1:
        t = load_file("Assignments/File_Assignment_4/employees.txt")
    elif choice == 2:
        save_file(t, "Assignments/File_Assignment_4/employees.txt")
    elif choice == 3:
        t = add_employee(t)
    elif choice == 4:
        index = int(
            input("Please enter the index of the employee you wish to delete: ")
        )
        t = delete_employee(t, index)
    elif choice == 5:
        t = modify_table(t)
    elif choice == 6:
        display_all(t)
