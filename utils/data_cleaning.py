from collections import defaultdict
import pandas as pd 
from .db_base_class import BookClubBase

class DataCleanser(BookClubBase):
    def __init__(self):
        self.initialize_data_structures()
    
    def initialize_data_structures(self):
        # Dictionary storing sets of reviewers for each book to track repeated reviews.
        # Key: Book Title | Value: Set of Review Authors
        self.repeated_reviews = defaultdict(set)

        # List to store all the book titles.
        self.titles = []

        # List to store all the member names.
        self.names = []

        # List to store all the ratings.
        self.ratings = []

    def remove_repeated_reviews(self, book_club_db):
        """
        Cleans the database by eliminating repeated reviews by the same member for the same book.
        Parameters:
            book_club_db (dataframe)
            
        Returns:
            book_club_db (dataframe): The dataframe without repeated reviews from the same author of the same book.
        """

        for title, member, rating in zip(reversed(book_club_db[self.DF_INDEX.title]), 
                                        reversed(book_club_db[self.DF_INDEX.name]), 
                                        reversed(book_club_db[self.DF_INDEX.rating])):

            
            if member in self.repeated_reviews[title]:
                continue

            # Update member review history
            self.repeated_reviews[title].add(member)

            # Add Unreviewed Books
            self.titles.append(title)
            self.names.append(member)
            self.ratings.append(rating)

        cleaned_df = pd.DataFrame(list(zip(self.titles, self.names, self.ratings)), columns=self.HEADER_NAMES)
        return cleaned_df