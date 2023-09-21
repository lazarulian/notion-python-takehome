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

class OptimizedRatingsAnalyzer(BookClubBase):
    def __init__(self):
        self.clean_data_structures()
    
    def clean_data_structures(self):
        # Dictionary storing sets of reviewers for each book to track repeated reviews.
        # Key: Book Title | Value: Set of Review Authors
        self.repeated_reviews = defaultdict(set)
        
        # Counter for accumulating rating scores for each book.
        # Key: Book Title | Value: Cumulative Rating Score
        self.ratings_sum = Counter()

        # Counter for tracking the number of times each book was marked as a favorite.
        # Key: Book Title | Value: Cumulative Favorite Count
        self.favorites_sum = Counter()

        # Counter for tracking the number of ratings each book received.
        # Key: Book Title | Value: Number of Ratings Received
        self.title_sum = Counter()

        # List to store all the book titles.
        self.titles = []

        # List to store all the member names.
        self.names = []

        # List to store all the ratings.
        self.ratings = []

    

    def optimized_extraction(self, book_club_db):
        """
        Analyzes and extracts various metrics from the book club database in one pass.
        
        Specifically, this function does the following:
        1. Cleans the database by eliminating repeated reviews by the same member for the same book.
        2. Computes the number of times each book has been rated as a favorite (rating of 5).
        3. Computes the cumulative sum of ratings for each book to facilitate average rating computation. 
        Note: The average can be later derived by dividing by the number of ratings for each book.
        
        Parameters:
            book_club_db (dict): A dictionary representing the book club data with keys for book titles, member names, and ratings.
            
        Returns:
            None: The function updates internal data structures but does not return a value.
        """
        self.clean_data_structures()

        for title, member, rating in zip(reversed(book_club_db[self.DF_INDEX.title]), 
                                        reversed(book_club_db[self.DF_INDEX.name]), 
                                        reversed(book_club_db[self.DF_INDEX.rating])):

            if member in self.repeated_reviews[title]:
                continue
            
            # Update member review history
            self.repeated_reviews[title].add(member)

            # Append to cleaned lists
            self.titles.append(title)
            self.names.append(member)
            self.ratings.append(rating)

            # Update statistics
            self.ratings_sum[title] += rating
            self.title_sum[title] += 1
            if rating == 5:
                self.favorites_sum[title] += 1
