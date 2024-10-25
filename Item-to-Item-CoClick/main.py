import pandas as pd
from itertools import combinations

# Read input file into pandas dataframe
clickstream_df = pd.read_csv("data/sample_clickstream.csv")

# List to store item pairs
item_pairs = []

# Find item pairs
for _, group in clickstream_df.groupby("user_id"):
    items = group["item_id"].unique()
    item_pairs.extend(combinations(items, 2))

# Create dataframe from item pairs list
# Add value count to it
# Sort it based on item1 name in ascending order and value count in descending order
item_pair_df = pd.DataFrame(item_pairs, columns=["item1", "item2"]).value_counts().reset_index(name="co_click")\
    .sort_values(["item1", "co_click"], ascending=[True, False])


# Find related items for item1
for item in item_pair_df["item1"].unique():
    related_items = item_pair_df[item_pair_df["item1"] == item]
    print("Related items for", item, ":", related_items["item2"].tolist())



