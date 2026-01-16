from datetime import date
import pytest

from src.banking import Account, AccountRepo, TransactionType


@pytest.fixture
def account_fixture():
    return Account(repo=AccountRepo())


def test_account_deposit(account_fixture):
    account_fixture.deposit(100)

    transaction = account_fixture.repo.all()[0]
    assert transaction.amount == 100
    assert transaction.type == TransactionType.DEPOSIT


def test_account_withdraw(account_fixture):
    account_fixture.withdraw(100)

    transaction = account_fixture.repo.all()[0]
    assert transaction.amount == 100
    assert transaction.type == TransactionType.WITHDRAWAL


def test_account_history(account_fixture):
    account_fixture.deposit(100)
    account_fixture.withdraw(50)
    account_fixture.deposit(200)

    history = account_fixture.history()

    today = date.today()
    assert history == [
        (today, 100, 100),
        (today, -50, 50),
        (today, 200, 250),
    ]
