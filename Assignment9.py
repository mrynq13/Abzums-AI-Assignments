
# 🏦 Bank Account Management System

# Task 1: BankAccount Class
class BankAccount:
    bank_name = "First National Bank"

    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    # Task 2: Deposit and Withdraw Methods
    def deposit(self, amount: float) -> None:
        if self.validate_amount(amount):
            self.balance += amount
            self.transactions.append(f"Deposit: +${amount}")
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount: float) -> None:
        if self.validate_amount(amount) and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount")

    # Task 3: Special and Class Methods
    def __str__(self) -> str:
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance}"

    @classmethod
    def change_bank_name(cls, new_name: str) -> None:
        cls.bank_name = new_name

    @staticmethod
    def validate_amount(amount: float) -> bool:
        return amount > 0

    # Task 5: Show Transaction History
    def show_transactions(self) -> None:
        if not self.transactions:
            print("No transactions yet.")
        else:
            print(f"Transaction history for {self.account_holder}:")
            for t in self.transactions:
                print(f" - {t}")

# Task 6: SavingsAccount Subclass
class SavingsAccount(BankAccount):
    def __init__(self, account_holder: str, initial_balance: float = 0.0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __str__(self) -> str:
        return f"Savings Account - Account Holder: {self.account_holder}, Balance: ${self.balance}, Interest Rate: {self.interest_rate * 100}%"

# Task 4: Test BankAccount
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

alice.deposit(200)
bob.withdraw(600)

print(alice)
print(bob)

print("Is -50 valid?", BankAccount.validate_amount(-50))

BankAccount.change_bank_name("Global Trust Bank")
print("Bank name changed to:", BankAccount.bank_name)

alice.show_transactions()
bob.show_transactions()

# Task 7: Test SavingsAccount
charlie = SavingsAccount("Charlie", 1000, interest_rate=0.05)
charlie.deposit(50)
charlie.add_interest()

print(charlie)
charlie.show_transactions()
