from datetime import datetime
from decimal import Decimal

import pytest

from functions.level_3.models import Expense, Currency, BankCard


@pytest.fixture
def make_bank_card():

    def _make_bank_card():
        return BankCard(last_digits="1234", owner="Mr Owner")

    return _make_bank_card


@pytest.fixture
def make_expense_at_date(make_bank_card):

    def _make_expense_at_date(amount: int,
                              spent_at: datetime,
                              currency=Currency.RUB.value,
                              ) -> Expense:
        return Expense(amount=Decimal(amount),
                       spent_at=spent_at,
                       currency=currency,
                       card=make_bank_card,
                       spent_in="Store Name",
                       category=None)

    return _make_expense_at_date
