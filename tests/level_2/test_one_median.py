import pytest

from functions.level_2.one_median import get_median_value


@pytest.mark.parametrize("items", [None, [], {}, False, 0, ""])
def test__get_median_value__returns_none(items):
    assert get_median_value(items) is None


@pytest.mark.parametrize("items", [
    [1, 2, None],
    [0, "1", 2],
    [None, None, None],
])
def test__get_median_value__list_of_incompatible_types(items):
    with pytest.raises(TypeError):
        get_median_value(items)


@pytest.mark.parametrize("items", [
    pytest.param([1], id="1 item"),
    pytest.param([1, 2], id="2 items"),
    pytest.param([1, 2, 3, 4], id="4 items"),
])
def test__get_median_value__raises_on_bad_length(items: list[int]):
    with pytest.raises(IndexError):
        get_median_value(items)


@pytest.mark.parametrize("items, median_expected", [
    ([5, 6, 7], 7),
    ([5, 6, 7, 8, 9], 8),
    ([5, 6, 7, 8, 9, 10], 9),
    ([5, 6, 7, 8, 9, 10, 15], 9),
])
def test__get_median_value__list_of_odd_len(items, median_expected):
    assert get_median_value(items) == median_expected
