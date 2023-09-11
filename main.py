"""
A script for basic csv analysis
"""
from pandas_script import (
    get_csv_stats,
    get_species_stats,
    save_species_count_plot,
    write_stats_to_markdown,
)


def main() -> None:
    """
    Print the statistics of the fish.csv file.
    Plot and save species counts.
    Save data stats to markdown.
    """
    print("Fish statistics")
    print(get_csv_stats())
    print("Species statistics")
    print(get_species_stats())
    save_species_count_plot()
    write_stats_to_markdown()


if __name__ == "__main__":
    main()
