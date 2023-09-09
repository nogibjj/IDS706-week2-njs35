"""
This script reads a CSV file from a URL and returns its statistics.
"""
import pandas as pd
from pandas import DataFrame


def get_fish_dataframe() -> DataFrame:
    """
    Read a CSV file from a URL and return its DataFrame.
    """
    return pd.read_csv("https://github.com/rickiepark/hg-mldl/raw/master/fish.csv")


def get_csv_stats() -> DataFrame:
    """
    Read a CSV file from a URL and return its statistics.
    """
    fish_df = get_fish_dataframe()
    stats = fish_df.describe()
    return stats


def get_species_stats() -> DataFrame:
    """
    Read a CSV file from a URL and return its statistics.
    """
    fish_df = get_fish_dataframe()
    species_stats = fish_df.groupby("Species").describe()
    return species_stats
