import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from__date_str_tomorrow(generate_datetime, date_str="tomorrow"):
    dt_expected = generate_datetime(delta_days=1)
    time_str = dt_expected.strftime("%H:%M")

    composed_dt = compose_datetime_from(date_str=date_str, time_str=time_str)

    assert composed_dt == dt_expected


@pytest.mark.parametrize("date_str", ["today", None, True, 0, ""])
def test_compose_datetime_from__date_str_other(generate_datetime, date_str):
    dt_expected = generate_datetime()
    time_str = dt_expected.strftime("%H:%M")

    composed_dt = compose_datetime_from(date_str=date_str, time_str=time_str)

    assert composed_dt == dt_expected


@pytest.mark.parametrize("time_str", [
    pytest.param("0010", id="no delimiter"),
    pytest.param("00-10", id="wrong delimiter"),
    pytest.param("25:00", id="too much hours"),
    pytest.param("12:61", id="too much minutes"),
    pytest.param("hh:mm", id="not integers"),
])
def test__compose_datetime_from__raises_ValueError(time_str: str):
    with pytest.raises(ValueError):
        compose_datetime_from(date_str="", time_str=time_str)


@pytest.mark.parametrize("time_str", [None, 123, [], True])
def test__compose_datetime_from__raises_AttributeError(time_str: str):
    with pytest.raises(AttributeError):
        compose_datetime_from(date_str="", time_str=time_str)
