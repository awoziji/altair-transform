"""
Evaluate vega expressions language
"""
import datetime as dt
from functools import reduce, wraps
import itertools
import math
import operator
import random
import sys
import time as timemod
from typing import Any, Callable, Dict, Optional, Pattern, Union, overload

import numpy as np
import pandas as pd
from dateutil import tz

from altair_transform.utils import evaljs


class _UndefinedType(object):
    def __repr__(self):
        return "undefined"


undefined = _UndefinedType()


def eval_vegajs(expression: str, datum: pd.DataFrame = None) -> pd.DataFrame:
    """Evaluate a vega expression"""
    namespace = {"datum": datum} if datum is not None else {}
    namespace.update(VEGAJS_NAMESPACE)
    return evaljs(expression, namespace)


def vectorize(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        series_args = [
            arg
            for arg in itertools.chain(args, kwargs.values())
            if isinstance(arg, pd.Series)
        ]
        if not series_args:
            return func(*args, **kwargs)
        else:
            index = reduce(operator.or_, [s.index for s in series_args])

            def _get(x, i):
                return x.get(i, math.nan) if isinstance(x, pd.Series) else x

            return pd.Series(
                [
                    func(
                        *(_get(arg, i) for arg in args),
                        **{k: _get(v, i) for k, v in kwargs.items()},
                    )
                    for i in index
                ],
                index=index,
            )

    if hasattr(func, "__annotations__"):
        wrapper.__annotations__ = {
            key: Union[pd.Series, val] for key, val in func.__annotations__.items()
        }
    return wrapper


# Type Checking Functions
@vectorize
def isArray(value: Any) -> bool:
    """Returns true if value is an array, false otherwise."""
    return isinstance(value, (list, np.ndarray))


@vectorize
def isBoolean(value: Any) -> bool:
    """Returns true if value is a boolean (true or false), false otherwise."""
    return isinstance(value, (bool, np.bool_))


@vectorize
def isDate(value: Any) -> bool:
    """Returns true if value is a Date object, false otherwise.

    This method will return false for timestamp numbers or
    date-formatted strings; it recognizes Date objects only.
    """
    return isinstance(value, dt.datetime)


@vectorize
def isDefined(value: Any) -> bool:
    """Returns true if value is a defined value, false if value equals undefined.

    This method will return true for null and NaN values.
    """
    # TODO: support implicitly undefined values?
    return value is not undefined


@vectorize
def isNumber(value: Any) -> bool:
    """Returns true if value is a number, false otherwise.

    NaN and Infinity are considered numbers.
    """
    return np.issubdtype(type(value), np.number)


@vectorize
def isObject(value: Any) -> bool:
    """Returns true if value is an object, false otherwise.

    Following JavaScript typeof convention, null values are considered objects.
    """
    return value is None or isinstance(value, dict)


@vectorize
def isRegExp(value: Any) -> bool:
    """
    Returns true if value is a RegExp (regular expression)
    object, false otherwise.
    """
    return isinstance(value, Pattern)


@vectorize
def isString(value: Any) -> bool:
    """Returns true if value is a string, false otherwise."""
    return isinstance(value, str)


@vectorize
def isValid(value: Any) -> bool:
    """Returns true if value is not null, undefined, or NaN."""
    return not (value is undefined or pd.isna(value))


# Type Coercion Functions
@vectorize
def toBoolean(value: Any) -> bool:
    """
    Coerces the input value to a boolean.
    Null values and empty strings are mapped to null.
    """
    return bool(value)


@vectorize
def toDate(value: Any) -> Optional[float]:
    """
    Coerces the input value to a Date instance.
    Null values and empty strings are mapped to null.
    If an optional parser function is provided, it is used to
    perform date parsing, otherwise Date.parse is used.
    """
    if isinstance(value, (float, int)):
        return value
    if value is None or value == "":
        return None
    return pd.to_datetime(value).timestamp() * 1000


@vectorize
def toNumber(value: Any) -> Optional[float]:
    """
    Coerces the input value to a number.
    Null values and empty strings are mapped to null.
    """
    if value is None or value == "":
        return None
    return float(value)


@vectorize
def toString(value: Any) -> Optional[str]:
    """
    Coerces the input value to a string.
    Null values and empty strings are mapped to null.
    """
    if value is None or value == "":
        return None
    if isinstance(value, float) and value % 1 == 0:
        return str(int(value))
    return str(value)


# Date/Time Functions
def now() -> float:
    """Returns the timestamp for the current time."""
    return round(timemod.time() * 1000, 0)


@overload
def datetime() -> dt.datetime:
    ...


@overload  # noqa: F811
def datetime(timestamp: float) -> dt.datetime:
    ...


@overload  # noqa: F811
def datetime(
    year: float,
    month: int,
    day: int = 0,
    hour: int = 0,
    min: int = 0,
    sec: int = 0,
    millisec: float = 0,
) -> dt.datetime:
    ...


@vectorize  # noqa: F811
def datetime(*args):
    """Returns a new Date instance.

    datetime()  # current time
    datetime(timestamp)
    datetime(year, month[, day, hour, min, sec, millisec])

    The month is 0-based, such that 1 represents February.
    """
    if len(args) == 0:
        return dt.datetime.now()
    elif len(args) == 1:
        return dt.datetime.fromtimestamp(0.001 * args[0])
    elif len(args) == 2:
        return dt.datetime(*args, 1)
    elif len(args) <= 7:
        args = list(map(int, args))
        args[1] += 1  # JS month is zero-based
        if len(args) == 2:
            args.append(0)  # Day is required in Python
        if len(args) == 7:
            args[6] = int(args[6] * 1000)  # milliseconds to microseconds
        return dt.datetime(*args)
    else:
        raise ValueError("Too many arguments")


@vectorize
def date(datetime: dt.datetime) -> int:
    """
    Returns the day of the month for the given datetime value, in local time.
    """
    return datetime.day


@vectorize
def day(datetime: dt.datetime) -> int:
    """
    Returns the day of the week for the given datetime value, in local time.
    """
    return (datetime.weekday() + 1) % 7


@vectorize
def year(datetime: dt.datetime) -> int:
    """Returns the year for the given datetime value, in local time."""
    return datetime.year


@vectorize
def quarter(datetime: dt.datetime) -> int:
    """
    Returns the quarter of the year (0-3) for the given datetime value,
    in local time.
    """
    return (datetime.month - 1) // 3


@vectorize
def month(datetime: dt.datetime) -> int:
    """
    Returns the (zero-based) month for the given datetime value, in local time.
    """
    return datetime.month - 1


@vectorize
def hours(datetime: dt.datetime) -> int:
    """
    Returns the hours component for the given datetime value, in local time.
    """
    return datetime.hour


@vectorize
def minutes(datetime: dt.datetime) -> int:
    """
    Returns the minutes component for the given datetime value, in local time.
    """
    return datetime.minute


@vectorize
def seconds(datetime: dt.datetime) -> int:
    """
    Returns the seconds component for the given datetime value, in local time.
    """
    return datetime.second


@vectorize
def milliseconds(datetime: dt.datetime) -> float:
    """
    Returns the milliseconds component for the given datetime value,
    in local time.
    """
    return datetime.microsecond / 1000


@vectorize
def time(datetime: dt.datetime) -> float:
    """Returns the epoch-based timestamp for the given datetime value."""
    return datetime.timestamp() * 1000


@vectorize
def timezoneoffset(datetime):
    # TODO: use tzlocal?
    raise NotImplementedError("timezoneoffset()")


@vectorize
def utc(
    year: int,
    month: int = 0,
    day: int = 1,
    hour: int = 0,
    min: int = 0,
    sec: int = 0,
    millisec: int = 0,
) -> float:
    """
    Returns a timestamp for the given UTC date.
    The month is 0-based, such that 1 represents February.
    """
    return (
        dt.datetime(
            int(year),
            int(month) + 1,
            int(day),
            int(hour),
            int(min),
            int(sec),
            int(millisec * 1000),
            tzinfo=dt.timezone.utc,
        ).timestamp()
        * 1000
    )


@vectorize
def utcdate(datetime: dt.datetime) -> int:
    """Returns the day of the month for the given datetime value, in UTC time."""
    return date(datetime.astimezone(tz.tzutc()))


@vectorize
def utcday(datetime: dt.datetime) -> int:
    """Returns the day of the week for the given datetime value, in UTC time."""
    return day(datetime.astimezone(tz.tzutc()))


@vectorize
def utcyear(datetime: dt.datetime) -> int:
    """Returns the year for the given datetime value, in UTC time."""
    return year(datetime.astimezone(tz.tzutc()))


@vectorize
def utcquarter(datetime: dt.datetime) -> int:
    """Returns the quarter of the year (0-3) for the given datetime value, in UTC time."""
    return quarter(datetime.astimezone(tz.tzutc()))


@vectorize
def utcmonth(datetime: dt.datetime) -> int:
    """Returns the (zero-based) month for the given datetime value, in UTC time."""
    return month(datetime.astimezone(tz.tzutc()))


@vectorize
def utchours(datetime: dt.datetime) -> int:
    """Returns the hours component for the given datetime value, in UTC time."""
    return hours(datetime.astimezone(tz.tzutc()))


@vectorize
def utcminutes(datetime: dt.datetime) -> int:
    """Returns the minutes component for the given datetime value, in UTC time."""
    return minutes(datetime.astimezone(tz.tzutc()))


@vectorize
def utcseconds(datetime: dt.datetime) -> int:
    """Returns the seconds component for the given datetime value, in UTC time."""
    return seconds(datetime.astimezone(tz.tzutc()))


def utcmilliseconds(datetime: dt.datetime) -> float:
    """Returns the milliseconds component for the given datetime value, in UTC time."""
    return milliseconds(datetime.astimezone(tz.tzutc()))


@vectorize
def dayFormat(day: int) -> str:
    """
    Formats a (0-6) weekday number as a full week day name, according to the current locale.
    For example: dayFormat(0) -> "Sunday".
    """
    days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ]
    return days[day % 7]


@vectorize
def dayAbbrevFormat(day: int) -> str:
    """
    Formats a (0-6) weekday number as an abbreviated week day name, according to the current locale.
    For example: dayAbbrevFormat(0) -> "Sun".
    """
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    return days[day % 7]


@vectorize
def format(value, specifier):
    """Formats a numeric value as a string. The specifier must be a valid d3-format specifier (e.g., format(value, ',.2f')."""
    raise NotImplementedError()


@vectorize
def monthFormat(month: int) -> str:
    """Formats a (zero-based) month number as a full month name, according to the current locale. For example: monthFormat(0) -> "January"."""
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return months[month % 12]


@vectorize
def monthAbbrevFormat(month: int) -> str:
    """Formats a (zero-based) month number as an abbreviated month name, according to the current locale. For example: monthAbbrevFormat(0) -> "Jan"."""
    months = [
        "Jan",
        "Feb",
        "Ma",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    return months[month % 12]


@vectorize
def timeFormat(value, specifier):
    """Formats a datetime value (either a Date object or timestamp) as a string, according to the local time. The specifier must be a valid d3-time-format specifier. For example: timeFormat(timestamp, '%A')."""
    raise NotImplementedError()


@vectorize
def timeParse(string, specifier):
    """Parses a string value to a Date object, according to the local time. The specifier must be a valid d3-time-format specifier. For example: timeParse('June 30, 2015', '%B %d, %Y')."""
    raise NotImplementedError()


@vectorize
def utcFormat(value, specifier):
    """Formats a datetime value (either a Date object or timestamp) as a string, according to UTC time. The specifier must be a valid d3-time-format specifier. For example: utcFormat(timestamp, '%A')."""
    raise NotImplementedError()


@vectorize
def utcParse(value, specifier):
    """Parses a string value to a Date object, according to UTC time. The specifier must be a valid d3-time-format specifier. For example: utcParse('June 30, 2015', '%B %d, %Y')."""
    raise NotImplementedError()


# String functions
@vectorize
def indexof(string: str, substring: str) -> int:
    """Returns the first index of substring in the input string."""
    return string.find(substring)


@vectorize
def lastindexof(string: str, substring: str) -> int:
    """Returns the last index of substring in the input string."""
    return string.rfind(substring)


@vectorize
def length(string: str) -> int:
    """Returns the length of the input string."""
    return len(string)


@vectorize
def lower(string: str) -> str:
    """Transforms string to lower-case letters."""
    return string.lower()


def pad(string: str, length: int, character: str = " ", align: str = "right"):
    """
    Pads a string value with repeated instances of a character
    up to a specified length. If character is not specified, a
    space (‘ ‘) is used. By default, padding is added to the end
    of a string. An optional align parameter specifies if padding
    should be added to the 'left' (beginning), 'center', or
    'right' (end) of the input string.
    """
    raise NotImplementedError()


@vectorize
def parseFloat(string: str) -> Optional[float]:
    """
    Parses the input string to a floating-point value.
    Same as JavaScript’s parseFloat.
    """
    # Javascript parses the first N valid characters.
    # TODO: use a more efficient approach?
    string = str(string).strip().split()[0]
    for end in range(len(string), 0, -1):
        substr = string[:end]
        try:
            return float(substr)
        except ValueError:
            pass
    return None


@vectorize
def parseInt(string: str, base: int = 10) -> Optional[int]:
    """
    Parses the input string to an integer value.
    Same as JavaScript’s parseInt.
    """
    # Javascript parses the first N valid characters.
    # TODO: use a more efficient approach?
    string = str(string).strip().split()[0]
    base = int(base)
    for end in range(len(string), 0, -1):
        substr = string[:end]
        try:
            return int(substr, base)
        except ValueError:
            pass
    return None


def replace(string: str, pattern: Union[str, Pattern], replacement: str) -> str:
    """
    Returns a new string with some or all matches of pattern replaced by a
    replacement string. The pattern can be a string or a regular expression.
    If pattern is a string, only the first instance will be replaced.
    Same as JavaScript’s String.replace.
    """
    raise NotImplementedError()


@vectorize
def slice_(s: str, start: int, end: Optional[int] = None) -> str:
    """
    Returns a section of string between the start and end indices.
    If the end argument is negative, it is treated as an offset from
    the end of the string (length(string) + end).
    """
    start = int(start)
    if end is not None:
        end = int(end)
    return s[start:end]


@vectorize
def split(s: str, sep: str, limit: int = -1):
    """
    Returns an array of tokens created by splitting the input string
    according to a provided separator pattern. The result can optionally
    be constrained to return at most limit tokens.
    """
    return s.split(sep, limit)


@vectorize
def substring(s: str, start: int, end: Optional[int] = None) -> str:
    """Returns a section of string between the start and end indices."""
    # TODO: match JS handling of end index
    start = int(start)
    if end is not None:
        end = int(end)
    return s[start:end]


@vectorize
def trim(s: str) -> str:
    """Returns a trimmed string with preceding and trailing whitespace removed."""
    return s.strip()


def truncate(
    string: str, length: int, align: str = "right", ellipsis: str = "…"
) -> str:
    """
    Truncates an input string to a target length. The optional align argument
    indicates what part of the string should be truncated:
    'left' (the beginning), 'center', or 'right' (the end).
    By default, the 'right' end of the string is truncated.
    The optional ellipsis argument indicates the string to use to indicate
    truncated content; by default the ellipsis character … (\u2026) is used.
    """
    raise NotImplementedError()


@vectorize
def upper(s: str) -> str:
    """Transforms string to upper-case letters."""
    return s.upper()


# Object functions
@vectorize
def merge(*objs: dict) -> dict:
    out = {}
    for obj in objs:
        out.update(obj)
    return out


# From https://vega.github.io/vega/docs/expressions/
VEGAJS_NAMESPACE: Dict[str, Any] = {
    # Constants
    "null": None,
    "true": True,
    "false": False,
    "undefined": undefined,
    "NaN": math.nan,
    "E": math.e,
    "LN2": math.log(2),
    "LN10": math.log(10),
    "LOG2E": math.log2(math.e),
    "LOG10E": math.log10(math.e),
    "MAX_VALUE": sys.float_info.max,
    "MIN_VALUE": sys.float_info.min,
    "PI": math.pi,
    "SQRT1_2": math.sqrt(0.5),
    "SQRT2": math.sqrt(2),
    # Type Checking
    "isArray": isArray,
    "isBoolean": isBoolean,
    "isDate": isDate,
    "isDefined": isDefined,
    "isNumber": isNumber,
    "isObject": isObject,
    "isRegExp": isRegExp,
    "isString": isString,
    "isValid": isValid,
    # Type Coercion
    "toBoolean": toBoolean,
    "toDate": toDate,
    "toNumber": toNumber,
    "toString": toString,
    # Control Flow Functions
    "if": lambda test, if_value, else_value: if_value if test else else_value,
    # Math Functions
    "isNaN": np.isnan,
    "isFinite": np.isfinite,
    "abs": np.abs,
    "acos": np.arccos,
    "asin": np.arcsin,
    "atan": np.arctan,
    "atan2": np.arctan2,
    "ceil": np.ceil,
    "clamp": np.clip,
    "cos": np.cos,
    "exp": np.exp,
    "floor": np.floor,
    "log": np.log,
    "max": vectorize(max),
    "min": vectorize(min),
    "pow": np.power,
    "random": random.random,
    "round": np.round,
    "sin": np.sin,
    "sqrt": np.sqrt,
    "tan": np.tan,
    # Date/Time Functions
    "now": now,
    "datetime": datetime,
    "date": date,
    "day": day,
    "year": year,
    "quarter": quarter,
    "month": month,
    "hours": hours,
    "minutes": minutes,
    "seconds": seconds,
    "milliseconds": milliseconds,
    "time": time,
    "timezoneoffset": timezoneoffset,
    "utc": utc,
    "utcdate": utcdate,
    "utcday": utcday,
    "utcyear": utcyear,
    "utcquarter": utcquarter,
    "utcmonth": utcmonth,
    "utchours": utchours,
    "utcminutes": utcminutes,
    "utcseconds": utcseconds,
    "utcmilliseconds": utcmilliseconds,
    # String Functions
    "indexof": indexof,
    "lastindexof": lastindexof,
    "length": length,
    "lower": lower,
    "pad": pad,
    "parseFloat": parseFloat,
    "parseInt": parseInt,
    "replace": replace,
    "slice": slice_,
    "split": split,
    "substring": substring,
    "trim": trim,
    "truncate": truncate,
    "upper": upper,
    # Formatting Functions
    "dayFormat": dayFormat,
    "dayAbbrevFormat": dayAbbrevFormat,
    "monthFormat": monthFormat,
    "monthAbbrevFormat": monthAbbrevFormat,
    # Object Functions
    "merge": merge,
    # TODOs:
    # Statistical Functions
    # Array Functions
    # RegExp Functions
    # Color functions
    # Data functions
}
