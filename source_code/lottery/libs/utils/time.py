from datetime import datetime, tzinfo, timedelta
import dateutil.parser as time_parser
from pytz import timezone

from django.utils.timezone import now as django_now, get_current_timezone


def current_date(tz=None, use_default_tz=False):
    return current_datetime(tz=tz, use_default_tz=use_default_tz).date()


def current_datetime(tz=None, use_default_tz=False):
    if not tz and use_default_tz:
        tz = get_current_timezone()
    if tz:
        return datetime.now().astimezone(tz)
    return django_now()


def convert_to_tz(value: datetime, tz=None, use_default_tz=True):
    if not tz and use_default_tz:
        tz = get_current_timezone()
    return value.astimezone(tz)


def current_timestamp():
    return current_datetime().timestamp()


def current_tt_seconds():
    return int(current_timestamp())


def current_tt_milliseconds():
    return int(current_timestamp()*1000)


def datetime_ago(days=0, hours=0, minutes=0, seconds=0, milliseconds=0):
    return current_datetime() - timedelta(
        days=days, hours=hours, minutes=minutes,
        seconds=seconds, milliseconds=milliseconds
    )


def datetime_future(days=0, hours=0, minutes=0, seconds=0, milliseconds=0):
    return current_datetime() + timedelta(
        days=days, hours=hours, minutes=minutes,
        seconds=seconds, milliseconds=milliseconds
    )


def get_future_datetime_from_now(days=0, hours=0, minutes=0, seconds=0):
    seconds = seconds or 0
    if days:
        seconds += days * 86400
    if hours:
        seconds += hours * 3600
    if minutes:
        seconds += minutes * 60

    return current_datetime() + timedelta(seconds=seconds)


def seconds_to_minute_str(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f'{minutes}:{seconds}'


def __prepare_timezone(tz='UTC'):
    if isinstance(tz, str):
        return timezone(tz)
    elif isinstance(tz, tzinfo):
        return tz
    else:
        raise TypeError("Time zone is not valid")


def parse_timestamp(timestamp, tz='UTC'):
    _result = None
    if isinstance(timestamp, (str, int, float)):
        _t = float(timestamp)
        _result = datetime.utcfromtimestamp(_t)
    elif isinstance(timestamp, datetime):
        _result = timestamp
    else:
        raise TypeError("Can not parse time from type[%s]" % type(timestamp))

    tz = __prepare_timezone(tz)
    return _result.astimezone(tz)


def parse_time_string(time_string, tz='UTC'):
    if isinstance(time_string, (int, str)):
        tz = __prepare_timezone(tz)
        return time_parser.parse(time_string).astimezone(tz)
    return time_string


def parse_time(time, tz='UTC'):
    if isinstance(time, (int, float)):
        return parse_timestamp(time, tz=tz)
    elif isinstance(time, str):
        return parse_time_string(time, tz=tz)
    return time
