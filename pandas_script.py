import pandas as pd


# Read the CSV file
fish_df = pd.read_csv("https://github.com/rickiepark/hg-mldl/raw/master/fish.csv")

stats = fish_df.describe()

print(stats)
