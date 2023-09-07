import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host, path, query_params, expected",
    [
        ("h", "p", {"q1": "v1", "q2": "v2"}, "h/p?q1=v1&q2=v2"),
        ("h", "p", {"q1": "v1"}, "h/p?q1=v1"),
        ("h", "p", {}, "h/p"),
        ("h", "p", None, "h/p"),
    ])
def test_build_url(host, path, query_params, expected):
    url = build_url(host, path, query_params)
    assert url == expected
