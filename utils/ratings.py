import pandas as pd
from collections import namedtuple

# Module Imports
from .db_base_class import BookClubBase
from .validation import InputValidator

class BookClubAggregator(BookClubBase):
    def __init__(self, book_club_csv):
        # Inputs: book_club_ratings (csv)
        self.__book_club_db = pd.read_csv(book_club_csv, header=None, names=BookClubAggregator.HEADER_NAMES)

        # Declare Parent Classes
        validator = InputValidator(self.__book_club_db)
        print(validator.validate_csv())
        
    
    def get_club_data(self):
        # Returns the book club raw data
        return self.__book_club_db