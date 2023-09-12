import decimal
import random
from datetime import datetime

import pytest

from functions.level_1.four_bank_parser import parse_ineco_expense


@pytest.mark.parametrize("amount", ["10", "10.99", "1 2 10", "1 2 10.1"])
@pytest.mark.parametrize("spent_in", ["ShopName", "1234"])
@pytest.mark.parametrize("spent_at", ["01.01.70 00:00", "31.12.70 23:59"])
def test__parse_ineco_expense__success(amount, spent_in, spent_at, gen_sms, gen_bank_card):
    card = gen_bank_card()
    sms = gen_sms(
        text=f"{amount} 10, 0000-0000-0000-{card.last_digits} {spent_at} {spent_in} authcode 1"
    )

    expense = parse_ineco_expense(sms=sms, cards=[card])

    assert expense.amount == decimal.Decimal(amount.split(" ")[-1])
    assert expense.card == card
    assert expense.spent_in == spent_in
    assert expense.spent_at == datetime.strptime(spent_at, "%d.%m.%y %H:%M")


def test__parse_ineco_expense__match_card(gen_sms, gen_bank_card):
    sample_card = gen_bank_card(last_digits=4444)
    other_cards = [gen_bank_card(last_digits=num) for num in range(1000, 1010)]
    cards_pool = [sample_card] + other_cards
    random.shuffle(cards_pool)
    sms = gen_sms(
        text=f"555 10, 0000-0000-0000-{sample_card.last_digits} 01.01.70 00:00 ShopName authcode 1"
    )

    expense = parse_ineco_expense(sms=sms, cards=cards_pool)

    assert expense.card == sample_card


@pytest.mark.parametrize("time_str", [
    pytest.param("01.13.70 00:00", id="too big month"),
    pytest.param("32.01.70 00:00", id="too big month day"),
    pytest.param("01.01.70 24:00", id="too much hours"),
    pytest.param("01.01.70 00:60", id="too much minutes"),
    pytest.param("01.01.70 00:60:01", id="with seconds"),
    pytest.param("01-01-70 00:60", id="wrong format #1"),
    pytest.param("01.01.70T00:60", id="wrong format #2"),
])
def test__parse_ineco_expence__invalid_time_format(gen_sms, gen_bank_card, time_str):
    card = gen_bank_card()
    sms = gen_sms(
        text=f"555 10, 0000-0000-0000-{card.last_digits} {time_str} ShopName authcode 1"
    )
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards=[card])


@pytest.mark.parametrize("sep", ["", " ", "-", "_"])
def test__parse_ineco_expence__unsplittable_text(sep, gen_sms, gen_bank_card):
    card = gen_bank_card()
    sms = gen_sms(
        text=f"555 10{sep} 0000-0000-0000-{card.last_digits} 01.01.70 00:00 ShopName authcode 1"
    )
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards=[card])


@pytest.mark.parametrize("raw_sum", ["1", "10", "10-99", "10:99", "10_99", "10.99", "10/99"])
def test__parse_ineco_expence__unsplittable_raw_sum(raw_sum, gen_sms, gen_bank_card):
    card = gen_bank_card()
    sms = gen_sms(
        text=f"{raw_sum}, 0000-0000-0000-{card.last_digits} 01.01.70 00:00 ShopName authcode 1"
    )
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards=[card])


@pytest.mark.parametrize("sep", ["", "-", "_"])
def test__parse_ineco_expence__unsplittable_raw_details(sep, gen_sms, gen_bank_card):
    card = gen_bank_card()
    raw_details = f"0000-0000-0000-{card.last_digits}{sep}01.01.70{sep}00:00{sep}ShopName"
    sms = gen_sms(text=f"555 10, {raw_details} authode 1")
    with pytest.raises(ValueError):
        parse_ineco_expense(sms, cards=[card])


def test__parse_ineco_expence__no_cards_provided(gen_sms):
    sms = gen_sms(
        text=f"555 10, 0000-0000-0000-1111 01.01.70 00:00 ShopName authcode 1"
    )
    with pytest.raises(IndexError):
        parse_ineco_expense(sms, cards=[])
