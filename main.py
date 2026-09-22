import sys
import argparse

from tracker import add_issue, list_issues, search_issues, close_issue, update_issue

def main():
    parser = argparse.ArgumentParser(
        description="CLI Issue Tracker"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True
    )

    subparsers.add_parser("list")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")

    search_parser = subparsers.add_parser("search")
    search_parser.add_argument("query")

    close_parser = subparsers.add_parser("close")
    close_parser.add_argument("title")

    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("old_title")
    update_parser.add_argument("new_title")




    args = parser.parse_args()

    if args.command == "add":
        try:
            issue = add_issue(args.title)
            print("Added:", issue)
        except ValueError as error:
            print("Error:", error)

    elif args.command == "list":
        issues = list_issues()

        for issue in issues:
            print("Title:", issue["title"])
            print("Status:", issue["status"])
            print("------")

    elif args.command == "search":
        results = search_issues(args.query)

        for issue in results:
            print("Title:", issue["title"])
            print("Status:", issue["status"])
            print("-----")

    elif args.command == "close":
        try:
            issue = close_issue(args.title)
            print("Closed:", issue)

        except ValueError as error:
            print("Error:", error)


    elif args.command == "update":
        try:
            issue = update_issue(
                args.old_title,
                args.new_title
            )

            print("Updated:", issue)

        except ValueError as error:
            print("Error:", error)

            

if __name__ == "__main__":
    main()









# if len (sys.argv) < 2:
#     print("Usage: python3 main.py <command>")
# else:
#     command = sys.argv[1]

#     if command == "list":
#         issues = list_issues()

#         for issue in issues:
#             print("Title:", issue["title"])
#             print("Status:", issue["status"])
#             print("---")

#     elif command == "add":
#         if len(sys.argv) < 3:
#             print('Usage: python3 man.py add "TITLE')
#         else:
#             title = sys.argv[2]

#             try:
#                 issue = add_issue(title)
#                 print("Added:", issue)

#             except ValueError as error:
#                 print("Error:", error)


#     elif command == "search":

#         if len(sys.argv) < 3:
#             print('Usage: python3 main.py search "QUERY"')
#         else:
#             query = sys.argv[2]

#             results = search_issues(query)

#             for issue in results:
#                 print("Title:", issue["titel"])
#                 print("Status:", issue["status"])
#                 print("---")

#     else:
#         print("Unknown command")

# # if there is no command:
# #     print usage

# # otherwise:
# #     get command

# #     if command is list:
# #         list issues

# #     elif command is add:
# #         if there is no title:
# #             print add usage
# #         else:
# #             add issue

# #     elif command is search:
# #         if there is no query:
# #             print search usage
# #         else:
# #             search

# #     else:
# #         print unknown command