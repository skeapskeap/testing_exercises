import pytest

from functions.level_3.models import ExpenseCategory
from functions.level_3.two_expense_categorizer import guess_expense_category, \
    is_string_contains_trigger


@pytest.fixture(params={" ", ",", ".", "-", "/", "\\"})
def delimiter(request):
    return request.param


@pytest.fixture
def trigger():
    return "trigger_val"


def test__is_string_contains_trigger__string_is_trigger(trigger):
    trigger = "trigger_val"
    assert is_string_contains_trigger(trigger, trigger)


@pytest.mark.parametrize("orig_string, _trigger", [
    pytest.param("trigger_val", "trigger_val", id="lower_case"),
    pytest.param("TRIGGER_VAL", "trigger_val", id="upper_case"),
    pytest.param("TriGgeR_Val", "trigger_val", id="various case"),
])
def test__is_string_contains_trigger__different_cases(orig_string: str, _trigger: str):
    assert is_string_contains_trigger(original_string=orig_string,
                                      trigger=_trigger)


def test__is_string_contains_trigger__string_starts_with_trigger(delimiter, trigger):
    assert is_string_contains_trigger(original_string=f"{delimiter}{trigger} string tail",
                                      trigger=trigger)


def test__is_string_contains_trigger__string_ends_with_trigger(delimiter, trigger):
    assert is_string_contains_trigger(original_string=f"string beginning {trigger}{delimiter}",
                                      trigger=trigger)


@pytest.mark.parametrize("left_delimiter", {" ", ",", ".", "-", "/", "\\"})
@pytest.mark.parametrize("right_delimiter", {" ", ",", ".", "-", "/", "\\"})
def test__is_string_contains_trigger__string_contains_trigger(left_delimiter, right_delimiter, trigger):
    original_string = f"string beginning {left_delimiter}{trigger}{right_delimiter} string tail"
    assert is_string_contains_trigger(original_string, trigger)


def test__is_string_contains_trigger__not_allowed_delimiter(trigger):
    delimiter = ":"
    original_string = f"string beginning {delimiter}{trigger}{delimiter} string tail"
    assert not is_string_contains_trigger(original_string, trigger)


def test__is_string_contains_trigger__string_not_contains_trigger():
    assert not is_string_contains_trigger("string value", "trigger_value")


@pytest.mark.parametrize("trigger, category", [
    ("-asador-", ExpenseCategory.BAR_RESTAURANT),
    ("-chinar-", ExpenseCategory.SUPERMARKET),
    ("-apple.com/bill-", ExpenseCategory.ONLINE_SUBSCRIPTIONS),
    ("-farm-", ExpenseCategory.MEDICINE_PHARMACY),
    ("-tomsarkgh-", ExpenseCategory.THEATRES_MOVIES_CULTURE),
    ("-gg platform-", ExpenseCategory.TRANSPORT),
])
def test__guess_expense_category__returns_category(trigger, category, make_expense_spent_in):
    spent_in = f"any {trigger} words"
    assert guess_expense_category(make_expense_spent_in(spent_in)) == category


@pytest.mark.parametrize("trigger", ["", "no_trigger_word_here"])
def test__guess_expense_category__returns_none(trigger, make_expense_spent_in):
    spent_in = f"any {trigger} words"
    assert guess_expense_category(make_expense_spent_in(spent_in)) is None
