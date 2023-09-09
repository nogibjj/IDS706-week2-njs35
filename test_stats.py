"""
Various tests for pandas data analysis.
"""
import pandas as pd
import os
import main
from pandas_script import get_csv_stats, get_fish_dataframe, get_species_stats


def test_get_fish_dataframe():
    """Test that get_fish_dataframe() returns a DataFrame."""
    assert isinstance(get_fish_dataframe(), pd.DataFrame)


def test_stats_type():
    """Test that get_csv_stats() returns accurate stats."""
    stats_df = get_csv_stats()
    assert int(stats_df.loc["mean", "Weight"]) == 398
    assert int(stats_df.loc["std", "Weight"]) == 357
    assert int(stats_df.loc["min", "Weight"]) == 0
    assert int(stats_df.loc["max", "Weight"]) == 1650


def test_species_stats():
    """Test that get_species_stats() returns accurate species specific stats."""
    species_stats_df = get_species_stats()
    assert int(species_stats_df.loc["Bream", ("Weight", "mean")]) == 617
    assert int(species_stats_df.loc["Whitefish", ("Weight", "mean")]) == 531
    assert int(species_stats_df.loc["Perch", ("Weight", "mean")]) == 382
    assert int(species_stats_df.loc["Pike", ("Weight", "mean")]) == 718
    assert int(species_stats_df.loc["Smelt", ("Weight", "mean")]) == 11
    assert int(species_stats_df.loc["Roach", ("Weight", "mean")]) == 152
    assert int(species_stats_df.loc["Parkki", ("Weight", "mean")]) == 154


def test_species_count_plot():
    """Test that save_species_count_plot() is saving a file."""
    main.save_species_count_plot()
    assert os.path.isfile("img/species_distribution.png")


def test_main(capsys):
    """Test that main() is printing an output."""
    main.main()
    captured = capsys.readouterr()
    assert captured.out.startswith("Fish statistics")
    assert "Species statistics" in captured.out
