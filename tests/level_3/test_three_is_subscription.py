from datetime import datetime

from functions.level_3.three_is_subscription import is_subscription


def test__is_subscription__returns_true(make_expense_with_defaults):
    expense = make_expense_with_defaults()
    history = [
        make_expense_with_defaults(spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(spent_at=datetime(2000, 2, 1)),
        make_expense_with_defaults(spent_at=datetime(2000, 3, 1)),
    ]
    assert is_subscription(expense, history) is True


def test__is_subscription__too_few_same_expenses(make_expense_with_defaults):
    expense = make_expense_with_defaults()
    history = [
        make_expense_with_defaults(spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(spent_at=datetime(2000, 2, 1)),
    ]
    assert not is_subscription(expense, history)


def test__is_subscription__too_often_payments(make_expense_with_defaults):
    expense = make_expense_with_defaults()
    history = [
        make_expense_with_defaults(spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(spent_at=datetime(2000, 1, 15)),
        make_expense_with_defaults(spent_at=datetime(2000, 1, 30)),
    ]
    assert not is_subscription(expense, history)


def test__is_subscription__spent_in_other_stores(make_expense_with_defaults):
    expense = make_expense_with_defaults()
    history = [
        make_expense_with_defaults(spent_in="store 1", spent_at=datetime(2000, 1, 1)),
        make_expense_with_defaults(spent_in="store 2", spent_at=datetime(2000, 2, 1)),
        make_expense_with_defaults(spent_in="store 3", spent_at=datetime(2000, 3, 1)),
    ]
    assert not is_subscription(expense, history)


def test__is_subscription__returns_false_with_no_history(make_expense_with_defaults):
    expense = make_expense_with_defaults()
    assert not is_subscription(expense, [])
