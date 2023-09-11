import pytest

from functions.level_1.two_date_parser import compose_datetime_from


def test_compose_datetime_from(date_test_case):
    composed_dt = compose_datetime_from(relative_day=date_test_case.relative_day,
                                        time_str=date_test_case.time_str)
    assert composed_dt == date_test_case.dt_expected


# @pytest.mark.parametrize("time_str", ["no_delimiter", "not:integers", "25:00", "00:61"])
@pytest.mark.parametrize('time_str', [
    pytest.param('00:61', id='large minutes number'),
    pytest.param('25:00', id='large hours number'),
])
def test_compose_datetime_from_raises(time_str):
    with pytest.raises(ValueError):
        compose_datetime_from(relative_day="", time_str=time_str)
