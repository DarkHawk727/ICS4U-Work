import numpy as np
from tabulate import tabulate

datatype = np.dtype([("Employee#", str, 4), ("Name", str, 16),
                     ("Marital Status", str, 1), ("Age", np.int32),
                     ("Salary", np.int32)])


def load_file(filepath):
    with open(filepath, "r") as data:
        table = np.loadtxt(data, dtype=datatype, skiprows=1)
    return table


def save_file(table, filepath):
	# TODO: Add format specifier for saving the textt.
	np.savetxt(filepath, table, fmt=datatype)


def add_employee(employee_number, name, maritial_status, age, salary, table):
	# TODO: Check to see if there are two duplicate employee ids
    temp_row = np.empty((1, ), dtype=datatype)
    temp_row["Employee#"] = employee_number
    temp_row["Name"] = name
    temp_row["Marital Status"] = maritial_status
    temp_row["Age"] = age
    temp_row["Salary"] = salary
    return np.append(table, temp_row)


def delete_employee(table, index):
	# TODO: Add out of bounds error catching
    return np.delete(table, index, 0)


def modify_table(employee_number, name, maritial_status, age, salary, table):
	# TODO: Check to see if there are two duplicate employee ids

	display_all(table)
	index = int(input("Please select the index of the employee you would like to modify: "))
	table[]
	pass


def display_all(table):
    headers = ["Employee Number", "Name", "Marital Status", "Age", "Salary"]
    pretty_table = tabulate(t,
                            headers,
                            tablefmt="fancy_grid",
                            numalign="center")
    print(pretty_table)

print(
"""1. Open File
2. Save File
3. Add a record
4. Delete a record
5. Modify a record
6. Display All
7. Quit""")
choice = 0	
while choice != 7:
	choice = int(input("Please enter a choice (1-7): "))
	if choice == 1:
		t = load_file("Assignments/File_Assignment_4/employees.txt")
	elif choice == 2:
		save_file(t, "employees.txt")
	elif choice == 3:
		employee_number = str(input("Please enter the employee number: "))
		name = str(input("Please enter the name ([First Initial].[Last Name]: "))
		maritial_status = str(input("Please enter the employee's maritial status (M or S): ")).upper()
		age = int(input("Please enter the age of the employee: "))
		salary = int(input("Please enter the employee's salary: ")) 
		t = add_employee(employee_number, name, maritial_status, age, salary,t)
	elif choice == 4:
		index = int(input("Please enter the index of the employee you wish to delete: "))
		t = delete_employee(t, index)
	elif choice == 5:
		# TODO: add modify record
		pass
	elif choice == 6:
		display_all(t)

