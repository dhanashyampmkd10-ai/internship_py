import json
from datetime import datetime
def log_call(func):
    def wrapper(*args):
        with open("log.txt", "a") as file:
            file.write(
                f"{datetime.now()} | {func.__name__} | Args: {args}\n"
            )
        return func(*args)
    return wrapper
@log_call
def add_expense(category, amount):
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []
    expenses.append({
        "category": category,
        "amount": amount
    })
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)
    print("Expense Added")
@log_call
def get_summary():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount
    return summary
@log_call
def view_all():
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except:
        expenses = []
    if not expenses:
        print("No Expenses Found")
    else:
        for expense in expenses:
            print(
                f"Category: {expense['category']}, Amount: {expense['amount']}"
            )
def read_logs():
    try:
        with open("log.txt", "r") as file:
            lines = file.readlines()
    except:
        print("No log file found")
        return
    counts = {}
    for line in lines:
        parts = line.split("|")
        function_name = parts[1].strip()
        if function_name in counts:
            counts[function_name] += 1
        else:
            counts[function_name] = 1
    print("\nFunction Call Counts")
    for name, count in counts.items():
        print(f"{name}: {count}")
while True:
    print("\n1. Add Expense")
    print("2. Summary")
    print("3. View All")
    print("4. Read Logs")
    print("5. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        add_expense(category, amount)
    elif choice == "2":
        summary = get_summary()
        print(summary)
    elif choice == "3":
        view_all()
    elif choice == "4":
        read_logs()
    elif choice == "5":
        print("Goodbye")
        break
    else:
        print("Invalid Choice")