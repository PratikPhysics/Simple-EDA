class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive.")
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive.")
            if amount > self.balance:
                raise ValueError("Insufficient funds.")
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        except ValueError as e:
            print(f"Error: {e}")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        try:
            if account_holder in self.accounts:
                raise ValueError("Account already exists.")
            self.accounts[account_holder] = BankAccount(account_holder, initial_balance)
            print(f"Account created for {account_holder} with initial balance of ${initial_balance}.")
        except ValueError as e:
            print(f"Error: {e}")

    def get_account(self, account_holder):
        try:
            if account_holder not in self.accounts:
                raise ValueError("Account does not exist.")
            return self.accounts[account_holder]
        except ValueError as e:
            print(f"Error: {e}")
            return None


# Example usage
if __name__ == "__main__":
    bank = BankingSystem()

    bank.create_account("Alice", 1000)
    bank.create_account("Bob", 500)

    alice_account = bank.get_account("Alice")
    bob_account = bank.get_account("Bob")

    if alice_account:
        alice_account.deposit(200)
        alice_account.withdraw(150)
        alice_account.check_balance()

    if bob_account:
        bob_account.deposit(-100)  # Invalid deposit
        bob_account.withdraw(600)  # Insufficient funds
        bob_account.check_balance()
