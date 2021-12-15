import numpy as np

filename = "Assignments/Test1/inventory.txt"
datatype = np.dtype(
    [
        ("Department", str, 16),
        ("admin_ipads", np.int32),
        ("admin_computers", np.int32),
        ("teacher_ipads", np.int32),
        ("teacher_computers", np.int32),
        ("student_ipads", np.int32),
        ("student_computers", np.int32),
    ]
)

inventory = np.loadtxt(filename, dtype=datatype)


def add_record(table):
    temp_row = np.empty((1,), dtype=datatype)

    department = str(input("Please enter the department name: "))
    admin_ipads = int(input("Please enter the number of Administrative IPads: "))
    admin_computers = int(
        input("Please enter the number of Administrative Computers: ")
    )
    teacher_ipads = int(input("Please enter the number of Teacher IPads: "))
    teacher_computers = int(input("Please enter the number of Teacher Computers: "))
    student_ipads = int(input("Please enter the number of Student IPads: "))
    student_computers = int(input("Please enter the number of Student Computers: "))

    temp_row["Department"] = department

    temp_row["admin_ipads"] = admin_ipads
    temp_row["admin_computers"] = admin_computers

    temp_row["teacher_ipads"] = teacher_ipads
    temp_row["teacher_computers"] = teacher_computers

    temp_row["student_ipads"] = student_ipads
    temp_row["student_computers"] = student_computers

    return np.append(table, temp_row)


def total_devices(table):
    sum_ipads = (
        table["admin_ipads"].sum()
        + table["teacher_ipads"].sum()
        + table["student_ipads"].sum()
    )
    sum_computers = (
        table["admin_computers"].sum()
        + table["teacher_computers"].sum()
        + table["student_computers"].sum()
    )
    return sum_ipads, sum_computers


def sum_columns(table):
    admin_ipad_sum = table["admin_ipads"].sum()
    admin_computer_sum = table["admin_computers"].sum()
    teacher_ipad_sum = table["teacher_ipads"].sum()
    teacher_computer_sum = table["teacher_computers"].sum()
    student_ipad_sum = table["student_ipads"].sum()
    student_computer_sum = table["student_computers"].sum()

    return (
        admin_ipad_sum,
        admin_computer_sum,
        teacher_ipad_sum,
        teacher_computer_sum,
        student_ipad_sum,
        student_computer_sum,
    )


def department_totals(table):
    ipads, computers = [], []
    departments = table["Department"]
    for row in range(table.shape[0]):
        department_ipad_sum = table[row][1] + table[row][3] + table[row][5]
        department_computer_sum = table[row][2] + table[row][4] + table[row][6]

        ipads.append(department_ipad_sum)
        computers.append(department_computer_sum)

        department_ipad_sum, department_computer_sum = 0, 0
    return ipads, computers, departments


print("Welcome to the Employee Database")
print("Please select an option from the menu below:")
print("1. Add Record")
print("2. Display total IPads and Computers")
print("3. Display column totals")
print("4. Display total devices by Department")
print("5. Exit")

choice = 0
while choice != 5:
    choice = int(input("Please enter a choice (1-5): "))
    if choice == 1:
        inventory = add_record(inventory)
    elif choice == 2:
        print("The total number of IPads is: {}.".format(total_devices(inventory)[0]))
        print(
            "The total number of computers is: {}.".format(total_devices(inventory)[1])
        )
    elif choice == 3:
        print(
            "The total number of Administrative IPads is {}.".format(
                sum_columns(inventory)[0]
            )
        )
        print(
            "The total number of Administrative computers is {}.".format(
                sum_columns(inventory)[1]
            )
        )
        print(
            "The total number of Teacher IPads is {}.".format(sum_columns(inventory)[2])
        )
        print(
            "The total number of Teacher computer is {}.".format(
                sum_columns(inventory)[3]
            )
        )
        print(
            "The total number of Student IPads is {}.".format(sum_columns(inventory)[4])
        )
        print(
            "The total number of Student computers is {}.".format(
                sum_columns(inventory)[5]
            )
        )
    elif choice == 4:
        department_names = department_totals(inventory)[2]
        for i in range(len(department_names)):
            print(
                "The {} department has {} IPads.".format(
                    department_names[i], department_totals(inventory)[0][i]
                )
            )
            print(
                "The {} department has {} computers.".format(
                    department_names[i], department_totals(inventory)[1][i]
                )
            )
