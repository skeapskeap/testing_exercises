import pytest

from functions.level_2.three_first import first


@pytest.mark.parametrize("items", [
    pytest.param({1}, id="items is set"),
    pytest.param({True}, id="items is True"),
    pytest.param(123, id="items is number"),
])
def test__first__raises_type_error(items):
    with pytest.raises(TypeError):
        first(items)


@pytest.mark.parametrize("items", [
    pytest.param({1: "1"}, id="items is dict"),
])
def test__first__raises_key_error(items):
    with pytest.raises(KeyError):
        first(items)


@pytest.mark.parametrize("items, expected", [
    ([1, 2, 3], 1),
    ((10, 20, 30), 10),
    ({1: "one", 0: "zero"}, "zero"),
    ("string", "s"),
])
def test__first__returns_first(items, expected):
    assert first(items) == expected


@pytest.mark.parametrize("items", [
    pytest.param([], id="items is empty list"),
    pytest.param(None, id="items is None"),
    pytest.param(False, id="items is False"),
    pytest.param(0, id="items is 0"),
])
def test__first__returns_default(items):
    def_val = "def_val"
    assert first(items, default=def_val) == def_val


def test__first__raises_attribute_error():
    with pytest.raises(AttributeError):
        first(items=[])
