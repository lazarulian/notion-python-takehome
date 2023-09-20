from .db_base_class import BookClubBase

class TextNormalizer(BookClubBase):
    def normalize_text(self, text_list):
        """
        Normalize a list of text by stripping whitespace and converting to lowercase.
        
        Parameters:
            text_list (list): A list of text strings to be normalized.
            
        Returns:
            list: A list of normalized text strings.
        """
        text_list = [text.strip() for text in text_list]
        text_list = [text.lower() for text in text_list]

        return text_list
    
    def normalize_db(self, book_club_db):
        titles = book_club_db[self.DF_INDEX.title]
        members = book_club_db[self.DF_INDEX.name]

        book_club_db[self.DF_INDEX.title] = self.normalize_text(titles)
        book_club_db[self.DF_INDEX.name] = self.normalize_text(members)

        return book_club_db