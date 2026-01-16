"""
Kata 6: Banking kata
Note: This is an advanced example where the solution requires knowledge of using
a mocking framework. The possible solution can also have an elaborated design.
Solve it only if you feel comfortable with mocking frameworks and designing
your code.

Create a simple bank application with features of depositing, withdrawing,
and printing account statements.

Constraints
1. Start with a class with the following structure

public class Account {
  public void deposit(int amount)
  public void withdraw(int amount)
  public void printStatement()
}
2. You are not allowed to add any other public methods in this class

3. Use Strings and Integers for dates and amounts (keep it simple)

4. Don't worry about the spacing in the statement printed in the console

Requirements
1. Deposit into Account

2. Withdraw from an Account

3. Print the Account statement to the console

DATE       | AMOUNT  | BALANCE
10/04/2014 | 500.00  | 1400.00
02/04/2014 | -100.00 | 900.00
01/04/2014 | 1000.00 | 1000.00

"""

from dataclasses import dataclass
from datetime import date
from enum import StrEnum


class TransactionType(StrEnum):
    DEPOSIT = "deposit"
    WITHDRAWAL = "withdrawal"


@dataclass
class Transaction:
    amount: int
    type: TransactionType
    created: date


class AccountRepo:
    def __init__(self) -> None:
        self.balance_history: list[Transaction] = []

    def save(self, transaction: Transaction):
        self.balance_history.append(transaction)

    def all(self) -> list[Transaction]:
        return self.balance_history


class Account:
    def __init__(self, repo: AccountRepo) -> None:
        self.repo = repo

    def deposit(self, amount: int):
        transaction = Transaction(
            amount=amount, type=TransactionType.DEPOSIT, created=date.today()
        )
        self.repo.save(transaction)

    def withdraw(self, amount: int):
        transaction = Transaction(
            amount=amount, type=TransactionType.WITHDRAWAL, created=date.today()
        )
        self.repo.save(transaction)

    def history(self):
        rows = []
        balance = 0
        for entry in self.repo.all():
            multiplier = 1 if entry.type == TransactionType.DEPOSIT else -1
            balance += entry.amount * multiplier
            rows.append((entry.created, multiplier * entry.amount, balance))
        return rows

    def print(self):
        header = ["DATE", "AMOUNT", "BALANCE"]

        print(header)

        for created, amount, balance in self.history():
            print(created, amount, balance)
