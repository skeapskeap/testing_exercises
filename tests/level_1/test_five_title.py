import pytest

from functions.level_1.five_title import change_copy_item

COPY_PREFIX = "Copy of"
CONJUNCTOR = " "


@pytest.mark.parametrize("test_title", [
    pytest.param("my_title", id="any custom title"),
    pytest.param(f"{COPY_PREFIX} my title", id="title starts with copy prefix"),
])
def test__change_copy_item__too_small_max_len(test_title: str):
    max_len_lte_resulting_title = len(test_title) + len(COPY_PREFIX) + len(CONJUNCTOR)
    title = change_copy_item(test_title, max_len_lte_resulting_title)
    assert title == test_title


def test__change_copy_item__add_prefix():
    test_title = "my_title"
    max_len_gt_resulting_title = len(test_title) + len(COPY_PREFIX) + len(CONJUNCTOR) + 1
    title = change_copy_item(test_title, max_len_gt_resulting_title)
    assert title == f"{COPY_PREFIX} {test_title}"


@pytest.mark.parametrize("test_title, expected", [
    (f"{COPY_PREFIX}test_title", f"{COPY_PREFIX}test_title (2)"),
    (f"{COPY_PREFIX}test_title (-1)", f"{COPY_PREFIX}test_title (-1) (2)"),
])
def test__change_copy_item__add_postfix(test_title: str, expected: str):
    max_len_gt_resulting_title = len(test_title) + len(COPY_PREFIX) + len(CONJUNCTOR) + 1
    title = change_copy_item(test_title, max_len_gt_resulting_title)
    assert title == expected


@pytest.mark.parametrize("test_title, expected", [
    (f"{COPY_PREFIX}test_title (0)", f"{COPY_PREFIX}test_title (1)"),
    (f"{COPY_PREFIX}test_title (1)", f"{COPY_PREFIX}test_title (2)"),
    (f"{COPY_PREFIX}test_title (2)", f"{COPY_PREFIX}test_title (3)"),
])
def test__change_copy_item__increment_postfix(test_title: str, expected: str):
    max_len_gt_resulting_title = len(test_title) + len(COPY_PREFIX) + len(CONJUNCTOR) + 1
    title = change_copy_item(test_title, max_len_gt_resulting_title)
    assert title == expected
