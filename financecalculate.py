import json

#I want to create the trasaction list here
transactions = []

def add_transaction():
    """Add a new transaction."""
    date = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = input("Enter the amount: ")
    type_ = input("Enter the type (income/expense): ").strip().lower()

    try:
        amount = float(amount)
        if type_ not in ['income', 'expense']:
            raise ValueError("Type must be 'income' or 'expense'")
        
        transaction = {
            'date': date,
            'description': description,
            'amount': amount,
            'type': type_
        }
        transactions.append(transaction)
        print("Transaction added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

def view_transactions():
    """View all transactions."""
    if not transactions:
        print("No transactions found.")
        return

    for tx in transactions:
        print(f"Date: {tx['date']}, Description: {tx['description']}, Amount: {tx['amount']}, Type: {tx['type']}")

def summarize_budget():
    """Print a summary of total income, expenses, and balance."""
    income = sum(tx['amount'] for tx in transactions if tx['type'] == 'income')
    expenses = sum(tx['amount'] for tx in transactions if tx['type'] == 'expense')
    balance = income - expenses

    print(f"Total Income: ${income:.2f}")
    print(f"Total Expenses: ${expenses:.2f}")
    print(f"Balance: ${balance:.2f}")

def save_to_file(filename):
    """Save transactions to a file."""
    with open(filename, 'w') as file:
        json.dump(transactions, file)
    print(f"Transactions saved to {filename}.")

def load_from_file(filename):
    """Load transactions from a file."""
    global transactions
    try:
        with open(filename, 'r') as file:
            transactions = json.load(file)
        print(f"Transactions loaded from {filename}.")
    except FileNotFoundError:
        print(f"No file found with the name {filename}.")
    except json.JSONDecodeError:
        print("Error reading the file. It might be corrupted.")

def main():
    """Main function to run the budget tracker."""
    filename = 'transactions.json'
    
    while True:
        print("\nPersonal Budget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Summarize Budget")
        print("4. Save to File")
        print("5. Load from File")
        print("6. Exit")

        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            summarize_budget()
        elif choice == '4':
            save_to_file(filename)
        elif choice == '5':
            load_from_file(filename)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
