import pytest

from functions.level_1.five_title import change_copy_item, COPY_PREFIX


@pytest.mark.parametrize(
    "title, max_len, expected",
    [
        ("test_title", 10, "test_title"),
        ("test_title", 10 + len(COPY_PREFIX), "test_title"),
        ("test_title", 10 + len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title"),
        (f"{COPY_PREFIX}test_title", 10 + len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title"),
        (f"{COPY_PREFIX}test_title", 10 + 2 * len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title (2)"),
        (f"{COPY_PREFIX}test_title (3)", 14 + 2 * len(COPY_PREFIX), f"{COPY_PREFIX}test_title (3)"),
        (f"{COPY_PREFIX}test_title (3)", 14 + 2 * len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title (4)"),
        (f"{COPY_PREFIX}test_title (0)", 14 + 2 * len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title (1)"),
        (f"{COPY_PREFIX}test_title (-1)", 15 + 2 * len(COPY_PREFIX) + 1, f"{COPY_PREFIX}test_title (-1) (2)"),
    ]
)
def test_change_copy_item(title, max_len, expected):
    res = change_copy_item(title, max_len)
    assert res == expected
