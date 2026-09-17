issues = [
    {
        "title" : "Login broken",
        "status" : "open"

    },
    {
        "title": "Search broken",
        "status": "closed"
    }
]

print(issues)

print("First issue:", issues[0])
print("First title:", issues[0]["title"])
print("Second status:", issues[1]["status"])

issues[0]["status"] = "closed"
print(issues)

new_issue = {
    "title": "Button missing",
    "status": "open"
}

issues.append(new_issue)

print(issues)