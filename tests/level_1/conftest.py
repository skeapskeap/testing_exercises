from datetime import datetime, timedelta
from decimal import Decimal
from typing import NamedTuple

import pytest

from functions.level_1.four_bank_parser import SmsMessage, BankCard, Expense


class BankTestCase(NamedTuple):
    sms: SmsMessage
    card: BankCard
    expect_expense: Expense


@pytest.fixture(name="generate_datetime")
def dt_generator():
    def generate_datetime(delta_days=0):
        return (
            datetime.now().replace(hour=12, minute=30, second=0, microsecond=0)
            + timedelta(days=delta_days)
        )
    return generate_datetime


@pytest.fixture(
    name="bank_test_case",
    params=[
        (1024, "4444", "ShopName", datetime(1970, 1, 1, 0, 0)),
    ]
)
def make_bank_testcase(request):
    amount, last_digits, spent_in, spent_at_dt = request.param
    spent_at = spent_at_dt.strftime('%d.%m.%y %H:%M')
    card = BankCard(last_digits=last_digits, owner="Name Surname")
    sms = SmsMessage(
        text=f"{amount} 00, 0000-0000-0000-{last_digits} {spent_at} {spent_in} authcode 1234",
        author="bank_name",
        sent_at=datetime.now())
    expense = Expense(Decimal(amount), card, spent_in, spent_at_dt)
    return BankTestCase(sms, card, expense)
