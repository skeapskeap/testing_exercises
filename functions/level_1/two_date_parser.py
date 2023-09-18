import datetime


def compose_datetime_from(date_str: str, time_str: str) -> datetime.datetime:
    """
    :param date_str: 'tomorrow' is the only allowed value yet
    :param time_str: expected string formatted as 'hh:mm'
    """
    date = datetime.date.today()
    if date_str == "tomorrow":
        date += datetime.timedelta(days=1)

    hour_str, minute_str = time_str.strip().split(":")
    return datetime.datetime(
        date.year,
        date.month,
        date.day,
        int(hour_str),
        int(minute_str),
    )
