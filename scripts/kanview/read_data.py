from tabulate import tabulate
import os

path = os.getcwd()

file = open(path + "/fhsu_payroll_data.json", "r")
result = file.read()
print(tabulate(result, headers=["Employee Name","Job Title","Overtime Pay","Total Gross Pay"], tablefmt='psql'))
file.close()
