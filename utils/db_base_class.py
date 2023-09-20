from collections import namedtuple

class BookClubBase:
    HEADER_NAMES = ['book_title', 'member_name', 'rating']
    DF_INDEX = namedtuple('DFIndex', ['title', 'name', 'rating'])("book_title", "member_name", "rating")