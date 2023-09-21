from utils.ratings import BookClubAggregator
import pandas as pd

TEST_FILE = "tests/data/ratings.csv"

c = BookClubAggregator(TEST_FILE)

print(c.get_analyzed_ratings())