import numpy as np
from tabulate import tabulate

headers = ["Employee Number", "Name", "Marital Status", "Age", "Salary"]
datatype = np.dtype([("Employee#", str, 4), ("Name", str, 16), ("Marital Status", str, 1), ("Age", np.int32), ("Salary", np.int32)])

with open("Assignments/File_Assignment_4/employees.txt", "r") as data:
    mfw = np.loadtxt(data, dtype=datatype, skiprows=1) 

def display_all(table): 
    for line in table:
        print(line) 

bruh = tabulate(mfw, headers, tablefmt="fancy_grid", numalign="center")

print(bruh)