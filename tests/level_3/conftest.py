from datetime import datetime
from decimal import Decimal

import pytest

from functions.level_3.models import Expense, Currency, BankCard


@pytest.fixture
def bank_card():
    return BankCard(last_digits="1234", owner="Mr Owner")


@pytest.fixture(params={" ", ",", ".", "-", "/", "\\"})
def delimiter(request):
    return request.param


@pytest.fixture
def trigger():
    return "trigger_val"


@pytest.fixture
def make_expense_with_defaults(bank_card):

    def _make_expense_with_defaults(amount=1,
                                    spent_at=None,
                                    currency=Currency.RUB,
                                    card=None,
                                    spent_in="Store Name",
                                    category=None,
                                    ) -> Expense:
        return Expense(amount=Decimal(amount),
                       spent_at=spent_at or datetime.now(),
                       currency=currency,
                       card=card or bank_card,
                       spent_in=spent_in,
                       category=category)

    return _make_expense_with_defaults
