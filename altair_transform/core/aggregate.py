import altair as alt
import pandas as pd
from .visitor import visit


@visit.register
def _(transform: alt.AggregateTransform, df: pd.DataFrame):
    groupby = transform['groupby']
    for aggregate in transform['aggregate']:
        op = aggregate['op'].to_dict()
        field = aggregate['field']
        col = aggregate['as']

        op = AGG_REPLACEMENTS.get(op, op)

        if groupby is alt.Undefined:
            df[col] = df[field].aggregate(op)
        else:
            result = df.groupby(groupby)[field].aggregate(op)
            result.name = col
            df = df.join(result, on=groupby)
    return df


def confidence_interval(x, level):
    from scipy import stats
    return stats.t.interval(level, len(x)-1, loc=x.mean(), scale=x.sem())


AGG_REPLACEMENTS = {
    'argmin': 'idxmin',
    'argmax': 'idxmax',
    'average': 'mean',
    'ci0': lambda x: confidence_interval(x, 0.05),
    'ci1': lambda x: confidence_interval(x, 0.95),
    'distinct': 'nunique',
    'stderr': 'sem',
    'stdev': 'std',
    'stdevp': lambda x: x.std(ddof=0),
    'missing': lambda x: x.isnull().sum(),
    'q1': lambda x: x.quantile(0.25),
    'q3': lambda x: x.quantile(0.75),
    'valid': 'count',
    'values': 'count',
    'variance': 'var',
    'variancep': lambda x: x.var(ddof=0)
}