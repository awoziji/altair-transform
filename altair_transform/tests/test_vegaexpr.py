import datetime as dt
import pytest
import numpy as np
from altair_transform.vegaexpr import eval_vegajs, undefined

# Most parsing is tested in the parser; here we just test a sampling of the
# variables and functions defined in the vegaexpr namespace.

EXPRESSIONS = {
    "null": None,
    "true": True,
    "false": False,
    "undefined": undefined,
    "2 * PI": 2 * np.pi,
    "1 / SQRT2": 1.0 / np.sqrt(2),
    "LOG2E + LN10": np.log2(np.e) + np.log(10),
    "isArray([1, 2, 3])": True,
    "isBoolean(false)": True,
    "isBoolean(true)": True,
    "isBoolean(1)": False,
    "isDate(datetime(2019, 1, 1))": True,
    "isDate('2019-01-01')": False,
    "isDefined(null)": True,
    "isDefined(undefined)": False,
    "isNumber(3.5)": True,
    "isNumber(now())": True,
    "isString('abc')": True,
    'isString("abc")': True,
    "isObject({a:2})": True,
    "isObject({'a':2})": True,
    "isValid(null)": False,
    "isValid(NaN)": False,
    "isValid(undefined)": False,
    "isValid(0)": True,
    "toBoolean(1)": True,
    "toBoolean(0)": False,
    "toDate('')": None,
    "toDate(null)": None,
    "toDate(1547510400000)": 1547510400000,
    "toDate('2019-01-15')": 1547510400000,
    "toNumber('1234.5')": 1234.5,
    "toNumber('')": None,
    "toNumber(null)": None,
    "toString(123)": "123",
    "toString(0.5)": "0.5",
    "toString('')": None,
    "toString(null)": None,
    "toString(123)": "123",
    "toString('123')": "123",
    'if(4 > PI, "yes", "no")': "yes",
    "pow(sin(PI), 2) + pow(cos(PI), 2)": 1,
    "floor(1.5) == ceil(0.5)": True,
    "max(1, 2, 3) == min(3, 4, 5)": True,
    "time(datetime(1546338896789))": 1546338896789,
    "isDate(datetime())": True,
    "datetime(1546329600000)": dt.datetime.fromtimestamp(1546329600),
    "datetime(2019, 0, 1)": dt.datetime(2019, 1, 1),
    "year(datetime(2019, 0, 1, 2, 34, 56, 789))": 2019,
    "quarter(datetime(2019, 0, 1, 2, 34, 56, 789))": 0,
    "month(datetime(2019, 0, 1, 2, 34, 56, 789))": 0,
    "date(datetime(2019, 0, 1, 2, 34, 56, 789))": 1,
    "day(datetime(2019, 0, 1, 2, 34, 56, 789))": 2,
    "hours(datetime(2019, 0, 1, 2, 34, 56, 789))": 2,
    "minutes(datetime(2019, 0, 1, 2, 34, 56, 789))": 34,
    "seconds(datetime(2019, 0, 1, 2, 34, 56, 789))": 56,
    "milliseconds(datetime(2019, 0, 1, 2, 34, 56, 789))": 789,
    "utc(2019, 0, 1, 2, 34, 56, 789)": 1546310096789,
    "utcyear(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 2019,
    "utcquarter(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 0,
    "utcmonth(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 0,
    "utcdate(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 1,
    "utcday(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 2,
    "utchours(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 2,
    "utcminutes(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 34,
    "utcseconds(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 56,
    "utcmilliseconds(datetime(utc(2019, 0, 1, 2, 34, 56, 789)))": 789,
}


@pytest.mark.parametrize("expression,expected", EXPRESSIONS.items())
def test_vegajs_expressions(expression, expected):
    result = eval_vegajs(expression)
    if isinstance(result, float):
        assert np.allclose(result, expected)
    else:
        assert result == expected
