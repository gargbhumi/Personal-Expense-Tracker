import csv
from datetime import datetime

# List to hold all expenses
expenses = []

# ---------- Add Expense ----------
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food/Travel/Other): ")
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter description: ")

    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }
    expenses.append(expense)
    print("✅ Expense added successfully!")

# ---------- View Expenses ----------
def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")

# ---------- Set and Track Budget ----------
def track_budget():
    try:
        budget = float(input("Enter your monthly budget: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    total_spent = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Expenses: ₹{total_spent}")
    if total_spent > budget:
        print("⚠️ You have exceeded your budget!")
    else:
        print(f"✅ You are within budget. Remaining: ₹{budget - total_spent}")

# ---------- Save Expenses to File ----------
def save_expenses(filename="expenses.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "category", "amount", "description"])
        writer.writeheader()
        writer.writerows(expenses)
    print(f"💾 Expenses saved to {filename}")

# ---------- Load Expenses from File ----------
def load_expenses(filename="expenses.csv"):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
        print(f"📂 Loaded expenses from {filename}")
    except FileNotFoundError:
        print("No saved expenses found. Starting fresh.")

# ---------- Main Menu ----------
def menu():
    load_expenses()  # Load existing expenses if available
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Track Budget")
        print("4. Save Expenses")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            track_budget()
        elif choice == "4":
            save_expenses()
        elif choice == "5":
            save_expenses()
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    menu()


