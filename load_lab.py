import json

with open("issues.json", "r") as file:
    issues = json.load(file)

print(issues)
print(type(issues))
print(type(issues[0]))
print(issues[0]["title"])    