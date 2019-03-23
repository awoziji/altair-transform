"""Tests of the timeunit utilities"""
from dateutil.tz import tzlocal
import pytest
import pytz

import pandas as pd

from altair_transform.utils import timeunit


@pytest.fixture
def dates():
    return pd.date_range('1999-12-31 12:00',
                         '2000-01-01 12:00',
                         freq='H')


@pytest.mark.parametrize('timezone', [None, tzlocal(), 'UTC'])
def test_datetime_roundtrip(dates, timezone):
    dates = dates.tz_localize(timezone)
    timestamp = timeunit.date_to_timestamp(dates)
    dates2 = timeunit.timestamp_to_date(timestamp,
                                        tz=(dates.tz is not None),
                                        utc=(dates.tz is pytz.UTC))
    assert dates2.equals(dates)
