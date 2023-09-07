from datetime import datetime, timedelta
from typing import NamedTuple

import pytest


class DateTestCase(NamedTuple):
    relative_day: str
    time_str: str
    dt_expected: datetime


@pytest.fixture(name="valid_date_test_case",
                params=["tomorrow", "today", None])
def make_date_testcase(request):
    dt_expected = datetime.now().replace(hour=12, minute=30, second=0, microsecond=0)
    relative_day = request.param
    if relative_day == "tomorrow":
        dt_expected += timedelta(days=1)
    time_str = dt_expected.strftime("%H:%M")
    return DateTestCase(relative_day, time_str, dt_expected)
