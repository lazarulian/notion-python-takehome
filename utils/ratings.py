import pandas as pd
from collections import namedtuple

# Module Imports
from .db_base_class import BookClubBase
from .validation import InputValidator
from .normalization import TextNormalizer

class BookClubAggregator(BookClubBase):
    def __init__(self, book_club_csv):
        self.__book_club_db = pd.read_csv(book_club_csv, header=None, names=BookClubAggregator.HEADER_NAMES)
        
        # Initialize Helper Classes
        self.validator = InputValidator(self.__book_club_db)
        self.normalizer = TextNormalizer()
    
    def process_csv(self):
        self.validator.validate_csv()
        self.__book_club_db = self.normalizer.normalize_db(self.__book_club_db)
        print(self.__book_club_db)
    
    def get_club_data(self):
        # Returns the book club raw data
        return self.__book_club_db