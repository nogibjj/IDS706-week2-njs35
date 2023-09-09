"""
A script for basic csv analysis
"""
from pandas_script import get_csv_stats, get_species_stats


def main() -> None:
    """Print the statistics of the fish.csv file."""
    print("Fish statistics")
    print(get_csv_stats())
    print("Species statistics")
    print(get_species_stats())


if __name__ == "__main__":
    main()
