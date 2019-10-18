import pytest

from altair_transform.extract import _encoding_to_transform
from typing import Any, Dict, List, NamedTuple


class _TestCase(NamedTuple):
    encoding: Dict[str, Dict[str, Any]]
    expected_encoding: Dict[str, Dict[str, Any]]
    expected_transform: List[Dict[str, Any]]


@pytest.mark.parametrize(
    _TestCase._fields,
    [
        _TestCase(
            encoding={"x": {"aggregate": "count", "type": "quantitative"}},
            expected_encoding={"x": {"field": "count", "type": "quantitative"}},
            expected_transform=[{"aggregate": [{"op": "count", "as": "count"}]}],
        ),
        _TestCase(
            encoding={"x": {"field": "foo", "bin": True, "type": "ordinal"}},
            expected_encoding={
                "x": {"field": "foo_binned", "type": "ordinal", "title": "foo (binned)"}
            },
            expected_transform=[{"bin": True, "field": "foo", "as": "foo_binned"}],
        ),
        _TestCase(
            encoding={
                "x": {"aggregate": "sum", "field": "people", "type": "quantitative"},
                "y": {"field": "age", "type": "ordinal"},
            },
            expected_encoding={
                "x": {"field": "sum_people", "type": "quantitative"},
                "y": {"field": "age", "type": "ordinal"},
            },
            expected_transform=[
                {
                    "aggregate": [{"op": "sum", "field": "people", "as": "sum_people"}],
                    "groupby": ["y"],
                }
            ],
        ),
        _TestCase(
            encoding={
                "x": {"aggregate": "count", "type": "quantitative"},
                "y": {"field": "age", "bin": {"maxbins": 10}, "type": "quantitative"},
            },
            expected_encoding={
                "x": {"field": "count", "type": "quantitative"},
                "y": {
                    "field": "age_binned",
                    "bin": "binned",
                    "type": "quantitative",
                    "title": "age (binned)",
                },
                "y2": {"field": "age_binned2"},
            },
            expected_transform=[
                {
                    "bin": {"maxbins": 10},
                    "field": "age",
                    "as": ["age_binned", "age_binned2"],
                },
                {
                    "aggregate": [{"op": "count", "as": "count"}],
                    "groupby": ["age_binned", "age_binned2"],
                },
            ],
        ),
        _TestCase(
            encoding={
                "x": {"aggregate": "count", "type": "quantitative"},
                "y": {"field": "age", "bin": True, "type": "ordinal"},
            },
            expected_encoding={
                "x": {"field": "count", "type": "quantitative"},
                "y": {
                    "field": "age_binned",
                    "type": "ordinal",
                    "title": "age (binned)",
                },
            },
            expected_transform=[
                {"bin": True, "field": "age", "as": "age_binned"},
                {
                    "aggregate": [{"op": "count", "as": "count"}],
                    "groupby": ["age_binned"],
                },
            ],
        ),
    ],
)
def test_extract_simple_aggregate(encoding, expected_encoding, expected_transform):
    encoding, transform = _encoding_to_transform(encoding)
    assert encoding == expected_encoding
    assert transform == expected_transform