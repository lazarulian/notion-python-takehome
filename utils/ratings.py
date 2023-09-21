import pandas as pd
from collections import namedtuple

# Module Imports
from .db_base_class import BookClubBase
from .validation import InputValidator
from .normalization import TextNormalizer
from .data_cleaning import DataCleanser
from .analytics import RatingsAnalyzer

class BookClubAggregator(BookClubBase):
    def __init__(self, book_club_csv):
        self.__book_club_db = pd.read_csv(book_club_csv, header=None, names=BookClubAggregator.HEADER_NAMES)
        
        # Initialize Helper Classes
        self.validator = InputValidator(self.__book_club_db)
        self.normalizer = TextNormalizer()
        self.janitor = DataCleanser()
        self.terrance_tao = RatingsAnalyzer()
    
    def __process_csv(self):
        self.validator.validate_csv()
        self.__book_club_db = self.normalizer.normalize_db(self.__book_club_db)
        self.__book_club_db = self.janitor.remove_repeated_reviews(self.__book_club_db)
    
    def get_analyzed_ratings(self):
        self.__process_csv()
        return self.terrance_tao.analyze_ratings(self.__book_club_db)
    
    def get_club_data(self):
        # Returns the book club raw data
        return self.__book_club_db