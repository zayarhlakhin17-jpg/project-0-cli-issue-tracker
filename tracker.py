from storage import load_issues, save_issues

def validate_title(title):
    cleaned = title.strip()

    if cleaned == "":
        raise ValueError("Title cannot be empty")

    return cleaned

def add_issue(title):
    clean_title = validate_title(title)

    issues = load_issues()

    new_issue = {
        "title" : clean_title,
        "status": "open"
    }

    issues.append(new_issue)

    save_issues(issues)

    return new_issue


def list_issues():
    issues = load_issues()

    return issues


def search_issues(query):
    issues = load_issues()
    results = []

    for issue in issues:
        if query.lower() in issue["title"].lower():
            results.append(issue)

    return results
     