from pydantic import BaseModel, ValidationError
class Expense(BaseModel):
    title: str
    amount: float
    category: str
expenses = []
def add_expense(title, amount, category):
    try:
        expense = Expense(
            title=title,
            amount=amount,
            category=category
                        )
        expenses.append(expense)
        print("Expense added successfully!")
    except ValidationError as e:
        print("Validation Error:")
        print(e)
add_expense("shirt", 1200, "clothing")
add_expense("petrol",1500, "trip")
add_expense("lunch", "500", "foood")
print("\nExpenses List")
for expense in expenses:
    print(
        f"Title: {expense.title}, "
        f"Amount: {expense.amount}, "
        f"Category: {expense.category}"
    )
    