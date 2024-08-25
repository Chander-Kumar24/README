import json
from collections import defaultdict

# Initialize the expenses list
expenses = []

def add_expense():
    """Add a new expense."""
    description = input("Enter the expense description: ")
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    
    category = input("Enter the expense category: ")

    expense = {
        'description': description,
        'amount': amount,
        'category': category
    }
    expenses.append(expense)
    print("Expense added successfully.")

def view_expenses():
    """View all recorded expenses."""
    if not expenses:
        print("No expenses recorded.")
        return

    print("\nRecorded Expenses:")
    for expense in expenses:
        print(f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}, Category: {expense['category']}")
    print()

def view_summary():
    """View total expenses by category."""
    if not expenses:
        print("No expenses recorded.")
        return

    summary = defaultdict(float)
    for expense in expenses:
        summary[expense['category']] += expense['amount']

    print("\nExpense Summary by Category:")
    for category, total in summary.items():
        print(f"Category: {category}, Total Amount: ${total:.2f}")
    print()

def save_expenses(filename):
    """Save expenses to a file."""
    with open(filename, 'w') as file:
        json.dump(expenses, file, indent=4)
    print(f"Expenses saved to {filename}.")

def load_expenses(filename):
    """Load expenses from a file."""
    global expenses
    try:
        with open(filename, 'r') as file:
            expenses = json.load(file)
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No such file: {filename}")
    except json.JSONDecodeError:
        print("Error decoding JSON. File may be corrupted.")

def main():
    """Main function to run the expense tracker."""
    filename = 'expenses.json'
    load_expenses(filename)

    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Save Expenses")
        print("5. Load Expenses")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            view_summary()
        elif choice == '4':
            save_expenses(filename)
        elif choice == '5':
            load_expenses(filename)
        elif choice == '6':
            print("Exiting...")
            save_expenses(filename)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
