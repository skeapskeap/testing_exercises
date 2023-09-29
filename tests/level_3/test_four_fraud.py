from datetime import datetime

import pytest

from functions.level_3.four_fraud import find_fraud_expenses


def test__find_fraud_expenses__returns_empty_list_for_no_history():
    assert find_fraud_expenses(history=[]) == []


def test__find_fraud_expenses__returns_empty_list_for_too_big_amount(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=5001),
        make_expense_with_defaults(amount=5001),
        make_expense_with_defaults(amount=5001),
    ]
    assert find_fraud_expenses(history) == []


def test__find_fraud_expenses__returns_empty_list_for_too_short_fraud_chain(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=10),
        make_expense_with_defaults(amount=10),
    ]
    assert find_fraud_expenses(history) == []


def test__find_fraud_expenses__returns_empty_list_spent_in_diff_places(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=10, spent_in="Store 1"),
        make_expense_with_defaults(amount=10, spent_in="Store 2"),
        make_expense_with_defaults(amount=10, spent_in="Store 3"),
    ]
    assert find_fraud_expenses(history) == []


def test__find_fraud_expenses__returns_empty_list_spent_at_diff_time(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 2)),
        make_expense_with_defaults(amount=10, spent_at=datetime(2000, 1, 3)),
    ]
    assert find_fraud_expenses(history) == []


def test__find_fraud_expenses__returns_empty_list_diff_amount(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=1),
        make_expense_with_defaults(amount=2),
        make_expense_with_defaults(amount=3),
    ]
    assert find_fraud_expenses(history) == []


@pytest.mark.xfail(reason="wrong comparison e.spent_in == spent_at")
def test__find_fraud_expenses__returns_whole_history_as_fraud(make_expense_with_defaults):
    history = [
        make_expense_with_defaults(amount=10),
        make_expense_with_defaults(amount=10),
        make_expense_with_defaults(amount=10),
    ]
    assert find_fraud_expenses(history) == history
