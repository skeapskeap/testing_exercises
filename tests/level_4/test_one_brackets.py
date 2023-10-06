import pytest

from functions.level_4.one_brackets import delete_remove_brackets_quotes


@pytest.mark.parametrize("name", [
    "test_name",
    "}test_name",
    "test_name}",
    " {test_name}",
])
def test__delete_remove_brackets_quotes__returns_original_name(name):
    assert delete_remove_brackets_quotes(name) == name


def test__delete_remove_brackets_quotes__index_error_on_empty_name():
    with pytest.raises(IndexError):
        delete_remove_brackets_quotes("")


@pytest.mark.parametrize("name, expected", [
    ("{}", ""),
    ("{1}", ""),
    ("{12}", ""),
    ("{123}", "2"),
    ("{_test_}", "test"),
])
def test__delete_remove_brackets_quotes__removes_more_than_needed(name, expected):
    assert delete_remove_brackets_quotes(name) == expected
