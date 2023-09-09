"""
This script reads a CSV file from a URL and returns its statistics.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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


def save_species_count_plot() -> None:
    """Save a bar plot of the species counts."""
    fish_df = get_fish_dataframe()
    species_counts = fish_df["Species"].value_counts()
    custom_palette = sns.color_palette("Set3", len(species_counts))
    _, ax = plt.subplots(figsize=(8, 6))
    species_counts.plot(kind="bar", ax=ax, color=custom_palette)
    ax.set_title("Distribution of Species")
    ax.set_xlabel("Species")
    ax.set_ylabel("Count")
    ax.set_xticklabels(
        species_counts.index, rotation=45, ha="right"
    )  
    for i, v in enumerate(species_counts):
        ax.text(
            i, v + 5, str(v), ha="center", va="bottom", fontsize=12, fontweight="bold"
        )
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.savefig("img/species_distribution.png", dpi=300)
