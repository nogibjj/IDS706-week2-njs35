from pandas_script import get_csv_stats


def test_stats_type():
    assert get_csv_stats().type == 'DataFrame'
