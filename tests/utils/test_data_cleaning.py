import pytest
import pandas as pd
from utils.data_cleaning import DataCleanser

class TestDataCleanser:
    @pytest.fixture
    def setup_analyzer(self):
        return DataCleanser()
    
    def test_no_repeats(self, setup_analyzer):
        """Test if function works correctly with no repeated reviews."""
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Being Mortal'],
            'member_name': ['Alice', 'Bob'],
            'rating': [5, 4.5]
        })
        cleaned_db = setup_analyzer.remove_repeated_reviews(book_club_db)
        
        assert len(cleaned_db) == 2
        assert not cleaned_db.duplicated(subset=['book_title', 'member_name']).any()
    
    def test_repeating_values(self, setup_analyzer):
        """Test if function removes repeated reviews by the same member for the same book."""
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Being Mortal', 'Circe'],
            'member_name': ['Alice', 'Bob', 'Alice'],
            'rating': [5, 4.5, 3]
        })
        cleaned_db = setup_analyzer.remove_repeated_reviews(book_club_db)
        
        assert len(cleaned_db) == 2
        assert not cleaned_db.duplicated(subset=['book_title', 'member_name']).any()

    def test_empty_input(self, setup_analyzer):
        """Test if function handles an empty dataframe."""
        book_club_db = pd.DataFrame(columns=['book_title', 'member_name', 'rating'])
        cleaned_db = setup_analyzer.remove_repeated_reviews(book_club_db)
        
        assert cleaned_db.empty

    def test_all_repeating(self, setup_analyzer):
        """Test if function returns an empty dataframe if all reviews are repeated."""
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Circe'],
            'member_name': ['Alice', 'Alice'],
            'rating': [5, 5]
        })
        cleaned_db = setup_analyzer.remove_repeated_reviews(book_club_db)
        
        assert len(cleaned_db) == 1
    
    def test__keeps_last_review(self, setup_analyzer):
        """Test if function only keeps the last review by a member for a book."""
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Circe', 'Being Mortal', 'Being Mortal'],
            'member_name': ['Alice', 'Alice', 'Bob', 'Bob'],
            'rating': [3, 5, 4, 2.5]
        })
        cleaned_db = setup_analyzer.remove_repeated_reviews(book_club_db)
        
        assert len(cleaned_db) == 2
        assert not cleaned_db.duplicated(subset=['book_title', 'member_name']).any()

        # Check that the last reviews were kept
        alice_circe_rating = cleaned_db[(cleaned_db['book_title'] == 'Circe') & (cleaned_db['member_name'] == 'Alice')]['rating'].iloc[0]
        bob_being_mortal_rating = cleaned_db[(cleaned_db['book_title'] == 'Being Mortal') & (cleaned_db['member_name'] == 'Bob')]['rating'].iloc[0]
        
        assert alice_circe_rating == 5
        assert bob_being_mortal_rating == 2.5


