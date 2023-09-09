'''
This script reads a CSV file from a URL and returns its statistics.
'''
import pandas as pd
from pandas import DataFrame


def get_csv_stats() -> DataFrame:
    '''
    Read a CSV file from a URL and return its statistics.
    '''
    fish_df = pd.read_csv("https://github.com/rickiepark/hg-mldl/raw/master/fish.csv")
    stats = fish_df.describe()
    return stats
