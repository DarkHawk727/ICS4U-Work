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
	np.savetxt(filepath, table)


def insert_employee(index, employee_number, name, maritial_status, age, salary,
                    table):
    temp_row = np.empty((1, ), dtype=datatype)
    temp_row["Employee#"] = employee_number
    temp_row["Name"] = name
    temp_row["Marital Status"] = maritial_status
    temp_row["Age"] = age
    temp_row["Salary"] = salary
    np.insert(table, index, temp_row, 0)


def delete_employee(table, index):
    np.delete(table, index, 0)


def modify_table(table):
	# TODO: Maybe, idk.... write the damn function. Just a thought....
	pass


def display_all(table):
    headers = ["Employee Number", "Name", "Marital Status", "Age", "Salary"]
    pretty_table = tabulate(t,
                            headers,
                            tablefmt="fancy_grid",
                            numalign="center")
    print(pretty_table)

choice = 0	
while choice != 7:
	choice = int(input("Please enter a choice (1-7): "))
	if choice == 1:
		t = load_file("employees.txt")
		choice = int(input("Please enter a choice (1-7): "))
	elif choice == 2:
		save_file(t, "employees.txt")
		choice = int(input("Please enter a choice (1-7): "))
	elif choice == 3:
		index = int(input("Pleae enter the index of where you want to insert the entry: "))
		employee_number = str(input("Please enter the employee number: "))
		name = str(input("Please enter the name ([First Initial].[Last Name]: "))
		maritial_status = str(input("Please enter the employee's maritial status (M or S): ")).upper()
		age = int(input("Please enter the age of the employee: "))
		salary = int(input("Please enter the employee's salary: ")) 
		insert_employee(index, employee_number, name, maritial_status, age, salary,t)
		choice = int(input("Please enter a choice (1-7): "))
	elif choice == 4:
		index = int(input("Please enter the index of the employee you wish to delete: "))
		delete_employee(t, index)
		choice = int(input("Please enter a choice (1-7): "))
	elif choice == 5:
		# TODO: add modify record
		choice = int(input("Please enter a choice (1-7): "))
		pass
	elif choice == 6:
		display_all(t)
		choice = int(input("Please enter a choice (1-7): "))
display_all(t)
