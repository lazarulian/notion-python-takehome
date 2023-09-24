from collections import defaultdict, Counter
import pandas as pd
from .db_base_class import BookClubBase

class RatingsAnalyzer(BookClubBase):
    def __init__(self):
        # Counter for accumulating rating scores for each book.
        self.ratings_sum = Counter()

        # Counter for tracking the number of times each book was marked as a favorite.
        self.favorites_sum = Counter()

        # Counter for tracking the number of ratings each book received.
        self.title_sum = Counter()

    def _process_ratings(self, book_club_db):
        """
        Helper method to process and categorize ratings from the book club database.
        """
        self.__init__()
        for title, member, rating in zip(book_club_db[self.DF_INDEX.title], book_club_db[self.DF_INDEX.name], book_club_db[self.DF_INDEX.rating]):
            self.ratings_sum[title] += rating
            self.title_sum[title] += 1
            if rating == 5:
                self.favorites_sum[title] += 1
            else:
                self.favorites_sum[title] += 0

    def analyze_ratings(self, book_club_db):
        self._process_ratings(book_club_db)

        averages = self.get_average_ratings()
        favorites = self.get_number_of_favorites()
        combined_df = averages.merge(favorites)
        
        return combined_df

    def get_number_of_favorites(self):
        df = pd.DataFrame.from_dict(self.favorites_sum, orient="index").reset_index()
        df = df.rename(columns={'index': self.DF_INDEX.title, 0: "number_favorites"})
        return df

    def get_average_ratings(self):
        average_ratings = {title: self.ratings_sum[title] / count for title, count in self.title_sum.items()}
        df = pd.DataFrame.from_dict(average_ratings, orient="index").reset_index()
        df = df.rename(columns={'index': self.DF_INDEX.title, 0: "average_rating"})
        return df
