Employees = [(101, "Ayush", 22),(102, "john", 29),(103, "jam", 23)]
print("------Print List------")
for i in Employees:
    print(i)

Employees[0] = (110, "David", 22)
print()
print("---Printing list after modification---")
for i in Employees:
    print(i)