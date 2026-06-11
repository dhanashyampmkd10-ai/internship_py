import json
from datetime import datetime
def log_call(func):
    def wrapper(*args):
        time_now = datetime.now()
        with open("log.txt", "a") as file:
            file.write(f"{time_now} - {func.__name__} - {args}\n")
        return func(*args)
    return wrapper
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)
@log_call
def add_expense(category, amount):
    expenses = load_expenses()
    expenses.append({
        "category": category,
        "amount": amount
    })
    save_expenses(expenses)
    print("Expense added!")
@log_call
def get_summary():
    expenses = load_expenses()
    summary = {}
    for expense in expenses:
        category = expense["category"]
        if category not in summary:
            summary[category] = 0
        summary[category] += expense["amount"]
    print("\nSummary:")
    for category, total in summary.items():
        print(f"{category}: ₹{total}")
@log_call
def view_all():
    expenses = load_expenses()
    print("\nAll Expenses:")
    for expense in expenses:
        print(expense)
def read_logs():
    counts = {}
    try:
        with open("log.txt", "r") as file:
            for line in file:
                parts = line.split(" - ")
                function_name = parts[1]
                counts[function_name] = counts.get(function_name, 0) + 1
        print("\nFunction Call Count:")
        for func, count in counts.items():
            print(func, ":", count)
    except FileNotFoundError:
        print("No logs found.")
while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
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
        get_summary()
    elif choice == "3":
        view_all()
    elif choice == "4"
        read_logs()
    elif choice == "5":
        print("Program Ended")
        break
    else:
        print("Invalid choice")