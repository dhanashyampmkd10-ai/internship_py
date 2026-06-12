import json
from datetime import datetime

def log_call(func)->callable:
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as l:
            l.write(
                f"{datetime.now()} | Function: {func.__name__} | Args: {args}\n"
            )
        return func(*args, **kwargs)
    return wrapper

def load_file()->list:
    try:
        with open("expences.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expences(expences:list)->list:
    with open("expences.json", "w") as f:
        json.dump(expences, f, indent=2)

@log_call
def add_expence(catagory: str, amount: float)->None:
    expences = load_file()
    expences.append({
        "catagory": catagory,
        "amount": amount
    })
    save_expences(expences)
    print("Expense Added Successfully!")

@log_call
def view_expence()->None:
    expences = load_file()

    if not expences:
        print("No expenses found.")
        return

    print("\nAll Expenses:")
    for expence in expences:
        print(
            f"Catagory: {expence['catagory']} | Amount: {expence['amount']}"
        )

@log_call
def get_summery()->None:
    expences = load_file()
    summery = {}

    for expence in expences:
        catagory = expence["catagory"]
        amount = expence["amount"]
        summery[catagory] = summery.get(catagory, 0) + amount

    print("\nExpense Summary:")
    for catagory, amount in summery.items():
        print(f"{catagory}: {amount}")

@log_call
def read_logs()->None:
    try:
        with open("log.txt", "r") as f:
            lines = f.readlines()

        count = {}

        for line in lines:
            if "Function:" in line:
                func_name = line.split("Function: ")[1].split(" |")[0]
                count[func_name] = count.get(func_name, 0) + 1

        print("\nFunction Call Count:")
        for func, times in count.items():
            print(f"{func}: {times} times")

    except FileNotFoundError:
        print("Log file not found.")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Get Summary")
    print("4. Read Logs")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        catagory = input("Enter catagory: ")
        amount = float(input("Enter amount: "))
        add_expence(catagory, amount)

    elif choice == "2":
        view_expence()

    elif choice == "3":
        get_summery()

    elif choice == "4":
        read_logs()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Please try again.")