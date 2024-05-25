transactions = []

def add_transaction(type, amount, category):
    """Add an income or expense transaction."""
    transaction = {
        'type': type,
        'amount': amount,
        'category': category
    }
    transactions.append(transaction)
    print(f"Added {type} of ${amount} in category '{category}'.")

def view_balance():
    """View the current balance."""
    balance = 0
    for transaction in transactions:
        if transaction['type'] == 'income':
            balance += transaction['amount']
        elif transaction['type'] == 'expense':
            balance -= transaction['amount']
    return balance

def display_transactions():
    """Display all transactions."""
    for transaction in transactions:
        print(f"{transaction['type'].capitalize()}: ${transaction['amount']} - Category: {transaction['category']}")

def main():
    while True:
        print("\nBudget Tracker Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Balance")
        print("4. Display Transactions")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            income_amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            add_transaction('income', income_amount, category)
        elif choice == '2':
            expenditure_amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            if expenditure_amount>income_amount:
                print("Insufficient funds")
                
            else:
                add_transaction('expense', expenditure_amount, category)
        elif choice == '3':
            balance = view_balance()
            print(f"Current balance: ${balance:.2f}")
        elif choice == '4':
            display_transactions()
        elif choice == '5':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()