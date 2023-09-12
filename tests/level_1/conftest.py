from datetime import datetime, timedelta

import pytest

from functions.level_1.four_bank_parser import SmsMessage, BankCard


@pytest.fixture(name="generate_datetime")
def dt_generator():
    def generate_datetime(delta_days=0):
        return (
            datetime.now().replace(hour=12, minute=30, second=0, microsecond=0)
            + timedelta(days=delta_days)
        )
    return generate_datetime


@pytest.fixture
def gen_sms():
    def _sms_generator(text):
        return SmsMessage(text=text, author="", sent_at=datetime.now())
    return _sms_generator


@pytest.fixture
def gen_bank_card():
    def _card_generator(last_digits=1234):
        return BankCard(last_digits=str(last_digits), owner="Name Surname")
    return _card_generator
