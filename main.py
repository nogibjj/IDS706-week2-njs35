"""
A script for basic csv analysis
"""
from pandas_script import get_csv_stats, get_species_stats, save_species_count_plot


def main() -> None:
    """
    Print the statistics of the fish.csv file.
    Plot and save species counts.
    """
    print("Fish statistics")
    print(get_csv_stats())
    print("Species statistics")
    print(get_species_stats())
    save_species_count_plot()


if __name__ == "__main__":
    main()
