import json

def load_issues(file_path="issues.json"):
    try:
        with open(file_path, "r") as file:
            loaded_issues = json.load(file)

        return loaded_issues

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


def save_issues(issues, file_path="issues.json"):
    with open(file_path, "w") as file:
        json.dump(issues, file, indent=2)    