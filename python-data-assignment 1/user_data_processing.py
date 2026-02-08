def calculate_average(scores):
    return sum(scores) / len(scores)


def has_admin_access(roles):
    return "admin" in roles


def main():
    users = [
        {
            "name": "Rahul",
            "scores": [60, 70, 80],
            "roles": {"user"}
        },
        {
            "name": "Anita",
            "scores": [90, 85, 88],
            "roles": {"admin", "editor"}
        }
    ]

    for user in users:
        avg = calculate_average(user["scores"])
        admin_access = has_admin_access(user["roles"])

        print("Name:", user["name"])
        print("Average Score:", avg)
        print("Admin Access:", admin_access)
        print("-------------------")


main()