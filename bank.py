import uuid


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password  # In real systems, use hashed passwords!
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        return f"User(name={self.name}, accounts={[acc.account_number for acc in self.accounts]})"


class Account:
    def __init__(self, user, balance=0.0):
        self.account_number = str(uuid.uuid4())[:8]
        self.user = user
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")
        return self.balance

    def transfer(self, target_account, amount):
        if amount > self.balance:
            print("Transfer failed: Insufficient funds.")
            return
        self.withdraw(amount)
        target_account.deposit(amount)
        print(f"Transferred ₹{amount} to Account {target_account.account_number}")


class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, name, password):
        if name in self.users:
            print("User already exists.")
            return None
        user = User(name, password)
        self.users[name] = user
        print(f"User '{name}' created successfully.")
        return user

    def authenticate(self, name, password):
        user = self.users.get(name)
        if user and user.password == password:
            print(f"User '{name}' authenticated.")
            return user
        print("Authentication failed.")
        return None

    def create_account_for_user(self, user, initial_balance=0.0):
        account = Account(user, initial_balance)
        user.add_account(account)
        print(f"Account {account.account_number} created for {user.name} with ₹{initial_balance}")
        return account


# --- DEMO USAGE ---

bank = Bank()

# Create users
alice = bank.create_user("Alice", "alice123")
bob = bank.create_user("Bob", "bob123")

# Authenticate users
alice_auth = bank.authenticate("Alice", "alice123")
bob_auth = bank.authenticate("Bob", "bob123")

# Create accounts
alice_account = bank.create_account_for_user(alice_auth, 5000)
bob_account = bank.create_account_for_user(bob_auth, 3000)

# Perform operations
alice_account.deposit(1500)
alice_account.withdraw(2000)
alice_account.check_balance()

# Transfer money from Alice to Bob
alice_account.transfer(bob_account, 1000)

# Final balances
alice_account.check_balance()
bob_account.check_balance()
