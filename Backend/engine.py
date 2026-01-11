# backend/engine.py

class BankEngine:
    def __init__(self, initial_balance: float = 1000.0):
        self.balance = initial_balance

    def deposit(self, amount: float):
        if amount <= 0:
            return False, "Amount must be positive"
        self.balance += amount
        return True, self.balance

    def withdraw(self, amount: float):
        if amount > self.balance:
            return False, "Insufficient funds"
        self.balance -= amount
        return True, self.balance