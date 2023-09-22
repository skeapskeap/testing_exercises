from datetime import datetime
from statistics import StatisticsError

import pytest

from functions.level_3.models import Currency
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses


def test__calculate_average_daily_expenses__ignore_different_currency(make_expense_at_date):
    assert calculate_average_daily_expenses([
        make_expense_at_date(10, datetime(2000, 1, 1), currency=Currency.RUB.value),
        make_expense_at_date(10, datetime(2000, 1, 1), currency=Currency.USD.value),
        make_expense_at_date(10, datetime(2000, 1, 2), currency=Currency.EUR.value),
    ]) == 15


def test__calculate_average_daily_expenses__accept_negative_amounts(make_expense_at_date):
    assert calculate_average_daily_expenses([
        make_expense_at_date(-1, datetime(2000, 1, 1)),
        make_expense_at_date(-2, datetime(2000, 1, 2)),
        make_expense_at_date(6, datetime(2000, 1, 3)),
    ]) == 1


def test__calculate_average_daily_expenses__raises_if_no_expenses(make_expense_at_date):
    with pytest.raises(StatisticsError):
        calculate_average_daily_expenses([])


def test__calculate_average_daily_expenses__return_zero_if_zero_amounts(make_expense_at_date):
    assert calculate_average_daily_expenses([
        make_expense_at_date(0, datetime(2000, 1, 1)),
        make_expense_at_date(0, datetime(2000, 1, 2)),
    ]) == 0


def test__calculate_average_daily_expenses__return_amount_of_any_day_if_they_equal(make_expense_at_date):
    assert calculate_average_daily_expenses([
        make_expense_at_date(4, datetime(2000, 1, 1)),
        make_expense_at_date(4, datetime(2000, 1, 2)),
        make_expense_at_date(4, datetime(2000, 1, 3)),
    ]) == 4


def test__calculate_average_daily_expenses__normal_work(make_expense_at_date):
    assert calculate_average_daily_expenses([
        make_expense_at_date(321, datetime(2000, 1, 1)),
        make_expense_at_date(876, datetime(2000, 1, 1)),
        make_expense_at_date(543, datetime(2000, 1, 2)),
        make_expense_at_date(165, datetime(2000, 1, 3)),
    ]) == 635
