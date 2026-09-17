import json


issues = [
    {
        "title": "Login broken",
        "status": "open"
    },
    {
        "title": "Search broken",
        "status": "closed"
    }
]

with open("issues.json", "w") as file:
    json.dump(issues, file)