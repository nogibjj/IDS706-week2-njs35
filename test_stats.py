from pandas_script import get_csv_stats
import pandas as pd


def test_stats_type():
    assert isinstance(get_csv_stats(), pd.DataFrame)
