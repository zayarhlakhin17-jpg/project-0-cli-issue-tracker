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


def close_issue(title):
    # 1. clean the title
    clean_title = validate_title(title)

    # 2. laod all saved issues
    issues = load_issues()

    # 3. collect every issue with the same title
    matches = []

    for issue in issues:
        if issue["title"].lower() == clean_title.lower():
            matches.append(issue)

    # 4. no matching issue
    if len(matches) == 0:
        raise ValueError("Issue not found")

    # 5. duplicate title = ambiguous
    if len(matches) > 1:
        raise ValueError("Multiple issues match this title")

    # 6. exactly one match
    matched_issue = matches[0]

    if matched_issue["status"] == "closed":
        raise ValueError("Issue is already closed")

    # 7. close it 
    matched_issue["status"] = "closed"

    # 8. save the updated full issue list
    save_issues(issues)

    # 9. give the closed issue back to the caller
    return matched_issue


def update_issue(old_title, new_title):
    # clean old title
    clean_old_title = validate_title(old_title)

    # clean new title
    clean_new_title = validate_title(new_title)

    # load all issues
    issues = load_issues()

    # find all issues matching old title
    matches=[]

    for issue in issues:
        if issue["title"].lower() == clean_old_title.lower():
            matches.append(issue)

     # if 0 matches
            # raise Issue not found

    if len(matches) == 0:
        raise ValueError("Issue not found")

    # if more than 1 match
        # raise duplicate/ambiguous error

    if len(matches) > 1:
        raise ValueError("Multiple issues match this title")


    # get the one matching issue

    matched_issue = matches[0]

    # if old title and new title are the same
        # raise error

    if matched_issue["title"].lower() == clean_new_title.lower():
        raise ValueError("New title must be different")

    # change issue["title"] to new title
    matched_issue["title"] = clean_new_title

    # save issues
    save_issues(issues)

    # return updated issue
    return matched_issue