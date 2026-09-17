issues = [
    "Issue 1\n",
    "Issue 2\n",
    "Issue 3\n"
]

with open("write_test.txt", "w") as file:
    file.writelines(issues)