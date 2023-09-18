import pytest

from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize("host, path, query_params, expected", [
    pytest.param("h", "p", None, "h/p", id="None query params"),
    pytest.param("h", "p", {}, "h/p", id="empty query params"),
    pytest.param("h", "p", [], "h/p", id="query params is empty list"),
    pytest.param("h", "p", "", "h/p", id="query params is empty string"),
    pytest.param("h", "p", False, "h/p", id="query params is False"),
    pytest.param("h", "p", 0, "h/p", id="query params is 0"),
    pytest.param("h", "p", {"q1": "v1"}, "h/p?q1=v1", id="one query param"),
    pytest.param("h", "p", {"q1": "v1", "q2": "v2"}, "h/p?q1=v1&q2=v2", id="many query params"),
])
def test__build_url__valid_query_params(host, path, query_params, expected):
    url = build_url(host, path, query_params)
    assert url == expected


@pytest.mark.parametrize("host, path, query_params, expected", [
    pytest.param("h", "p", [1], "h/p", id="query params is list"),
    pytest.param("h", "p", "string", "h/p", id="query params is string"),
    pytest.param("h", "p", True, "h/p", id="query params is True"),
    pytest.param("h", "p", 1, "h/p", id="query params is 1"),
])
def test__build_url__not_valid_query_params(host, path, query_params, expected):
    with pytest.raises(AttributeError):
        build_url(host, path, query_params)


@pytest.mark.parametrize("host, path, expected", [
    pytest.param(None, "path", "None/path", id="host is None"),
    pytest.param([1, 2], "path", "[1, 2]/path", id="host is list"),
    pytest.param(123, "path", "123/path", id="host is int"),
])
def test__build_url__host_wrong_type(host, path, expected):
    url = build_url(host_name=host, relative_url=path)
    assert url == expected


@pytest.mark.parametrize("host, path, expected", [
    pytest.param("host", None, "host/None", id="path is None"),
    pytest.param("host", [1, 2], "host/[1, 2]", id="path is list"),
    pytest.param("host", 123, "host/123", id="path is int"),
])
def test__build_url__path_wrong_type(host, path, expected):
    url = build_url(host_name=host, relative_url=path)
    assert url == expected
