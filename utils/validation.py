import pandas as pd
from collections import namedtuple

# Module Imports
from .db_base_class import BookClubBase

class InputValidator(BookClubBase):
    def __init__(self, book_club_db):
        self.__book_club_db = book_club_db
        self.__error_messages = {
            "title_type": "The book titles are not typed as strings.",
            "name_type": "The member names are not typed as strings.",
            "rating_type": "The ratings are not typed as floats or ints.",
            "rating_range": "Ratings should be between 0 and 5."
        }
    
    def validate_csv(self):
        self.validate_types()
        self.validate_rating_range()
        return True
    
    def validate_rating_range(self):
        """
        Validates that ratings are within the allowed range.
        Raises:
            ValueError: If any rating is outside the range 0-5.
        """
        for rating in self.__book_club_db[self.HEADER_NAMES[2]]:
            if rating < 0 or rating > 5:
                raise ValueError(self.__error_messages["rating_range"])
        
        return True

    def validate_types(self):
        """
        Validates the types of various fields in the book club database.
        Returns:
            bool: True if all types are valid, otherwise raises a ValueError.
        """
        self.__validate_title_type()
        self.__validate_name_type()
        self.__validate_rating_type()
        return True

    def __validate_title_type(self):
        for title in self.__book_club_db[self.HEADER_NAMES[0]]:
            if not isinstance(title, str):
                raise ValueError(self.__error_messages["title_type"])

    def __validate_name_type(self):
        for name in self.__book_club_db[self.HEADER_NAMES[1]]:
            if not isinstance(name, str):
                raise ValueError(self.__error_messages["name_type"])

    def __validate_rating_type(self):
        for rating in self.__book_club_db[self.HEADER_NAMES[2]]:
            if not isinstance(rating, (float, int)):
                raise ValueError(self.__error_messages["rating_type"])
