   
class Budget:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount, note=""):
        if amount > 0:
            self.balance += amount
            self.transactions.append((amount, note))
            return True
        return False

    def withdraw(self, amount, note=""):
        if amount > 0 and self.check_funds(amount):
            self.balance -= amount
            self.transactions.append((amount, note))
            return True
        return False

    def get_balance(self):
        return self.balance

    def check_funds(self, amount):
        return amount <= self.balance

    def get_transactions(self):
        return self.transactions


class Expense(Budget):
    def __init__(self, name, budget):
        super().__init__(name, 0)  # Initialize balance as 0
        self.budget = budget

    def get_budget(self):
        return self.budget

    def get_balance_left(self):
        return self.budget - self.balance


def main():
    try:
        # Create an expense budget
        expense_budget = Expense("Expense", int(input("Enter your budget:")))

        # Deposit money into the expense budget
        if expense_budget.deposit(int(input("Enter amount deposited:")), "Money deposited"):
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

        # Withdraw money from the expense budget
        if expense_budget.withdraw(int(input("Enter amount withdrawn:")), "Money spent"):
            print("Withdrawal successful")
        else:
            print("Insufficient funds or invalid withdrawal amount")

        # Get the balance of the expense budget
        print("Current balance:", expense_budget.get_balance())

        # Get the budget of the expense budget
        print("Budget:", expense_budget.get_budget())

        # Get the balance left in the expense budget
        print("Balance left:", expense_budget.get_balance_left())

        # Get the transactions of the expense budget
        print("Transactions:", expense_budget.get_transactions())

    except:
        print("wrong input , try again")
        main()


if __name__ == '__main__':
    main()

# added try catch....
