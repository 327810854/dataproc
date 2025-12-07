import pandas as pd
from dataproc.tabular.proc import drop_empty, fill_empty

def test_drop_empty_any():
    df = pd.DataFrame({"a":[1, None], "b":[2, 3]})
    out = drop_empty(df, how='any')
    assert len(out) == 1

def test_drop_empty_all():
    df = pd.DataFrame({"a":[None, None], "b":[None, 3]})
    out = drop_empty(df, how='all')
    assert len(out) == 1

def test_fill_empty_value():
    df = pd.DataFrame({"a":[1, None], "b":[None, 2]})
    out = fill_empty(df, value=0)
    assert out.isnull().sum().sum() == 0

def test_fill_empty_method():
    df = pd.DataFrame({"a":[1, None, 2]})
    out = fill_empty(df, method='ffill')
    assert out.iloc[1,0] == 1