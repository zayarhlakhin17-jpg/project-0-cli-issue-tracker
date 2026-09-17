with open("practice.txt") as file:
    print("Inside: ")
    print("Name:", file.name)
    print("Mode:", file.mode)
    print("Closed:", file.closed)

print("Outside:")
print("Closed:", file.closed)