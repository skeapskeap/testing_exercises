from datetime import datetime
from statistics import StatisticsError

import pytest

from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__ignore_different_currency(make_expense_with_defaults):
    assert calculate_average_daily_expenses([
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 1), currency=Currency.RUB.value),
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 1), currency=Currency.USD.value),
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 2), currency=Currency.EUR.value),
    ]) == 15


def test__calculate_average_daily_expenses__accept_negative_amounts(make_expense_with_defaults):
    assert calculate_average_daily_expenses([
        make_expense_with_defaults(amount=-1, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=-2, spent_at=datetime(2000, 1, 2)),
        make_expense_with_defaults(amount=6, spent_at=datetime(2000, 1, 3)),
    ]) == 1


def test__calculate_average_daily_expenses__raises_if_no_expenses():
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])


def test__calculate_average_daily_expenses__return_zero_if_zero_amounts(make_expense_with_defaults):
    assert calculate_average_daily_expenses([
        make_expense_with_defaults(amount=0, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=0, spent_at=datetime(2000, 1, 2)),
    ]) == 0


def test__calculate_average_daily_expenses__return_amount_of_any_day_if_they_equal(make_expense_with_defaults):
    assert calculate_average_daily_expenses([
        make_expense_with_defaults(amount=4, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=4, spent_at=datetime(2000, 1, 2)),
        make_expense_with_defaults(amount=4, spent_at=datetime(2000, 1, 3)),
    ]) == 4


def test__calculate_average_daily_expenses__normal_work(make_expense_with_defaults):
    assert calculate_average_daily_expenses([
        make_expense_with_defaults(amount=321, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=876, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=543, spent_at=datetime(2000, 1, 2)),
        make_expense_with_defaults(amount=165, spent_at=datetime(2000, 1, 3)),
    ]) == 635
