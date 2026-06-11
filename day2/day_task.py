import json
from datetime import datetime

def log_call(func):
    def wrapper(*args):
        with open("log.txt", "a") as f:
            f.write(f"{datetime.now()} - {func.__name__} - {args}\n")
        return func(*args)
    return wrapper

@log_call
def add_expense(category, amount):
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

    expenses.append({"category": category, "amount": amount})

    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=2)

    print("Expense Added!")

@log_call
def get_summary():
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

    summary = {}

    for expense in expenses:
        category = expense["category"]

        if category in summary:
            summary[category] += expense["amount"]
        else:
            summary[category] = expense["amount"]

    return summary

@log_call
def view_all():
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []

    for expense in expenses:
        print(expense)

def read_logs():
    count = {}

    try:
        with open("log.txt", "r") as f:
            for line in f:
                if "add_expense" in line:
                    count["add_expense"] = count.get("add_expense", 0) + 1
                elif "get_summary" in line:
                    count["get_summary"] = count.get("get_summary", 0) + 1
                elif "view_all" in line:
                    count["view_all"] = count.get("view_all", 0) + 1

        print("\nFunction Calls:")
        for key, value in count.items():
            print(key, ":", value)

    except FileNotFoundError:
        print("No logs found")

while True:
    print("\n1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Read Logs")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = float(input("Enter amount: "))
        add_expense(category, amount)

    elif choice == "2":
        result = get_summary()
        print(result)

    elif choice == "3":
        view_all()

    elif choice == "4":
        read_logs()

    elif choice == "5":
        break

    else:
        print("Invalid Choice")