import pytest
import pandas as pd
from utils.analytics import RatingsAnalyzer

class TestRatingsAnalyzer:
    @pytest.fixture
    def setup_analyzer(self):
        return RatingsAnalyzer()

    def test_analyze_ratings(self, setup_analyzer):
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Being Mortal', 'Circe'],
            'member_name': ['Alice', 'Bob', 'Alice'],
            'rating': [5, 3.5, 5]
        })

        combined_df = setup_analyzer.analyze_ratings(book_club_db)

        # Check if average rating is computed correctly
        assert combined_df[combined_df['book_title'] == 'Circe']['average_rating'].iloc[0] == 5
        assert combined_df[combined_df['book_title'] == 'Being Mortal']['average_rating'].iloc[0] == 3.5
        
        # Check if number of favorites is computed correctly
        assert combined_df[combined_df['book_title'] == 'Circe']['number_favorites'].iloc[0] == 2
        assert combined_df[combined_df['book_title'] == 'Being Mortal']['number_favorites'].iloc[0] == 0

    def test_analyze_ratings_empty_df(self, setup_analyzer):
        """Test when book_club_db is empty."""
        book_club_db = pd.DataFrame(columns=['book_title', 'member_name', 'rating'])
        combined_df = setup_analyzer.analyze_ratings(book_club_db)
        
        assert combined_df.empty

    def test_analyze_ratings_no_favorites(self, setup_analyzer):
        """Test when no book has been marked as a favorite."""
        book_club_db = pd.DataFrame({
            'book_title': ['Circe', 'Being Mortal'],
            'member_name': ['Alice', 'Bob'],
            'rating': [4, 4.5]
        })
        
        combined_df = setup_analyzer.analyze_ratings(book_club_db)
        
        # Check if average rating is computed correctly
        assert combined_df[combined_df['book_title'] == 'Circe']['average_rating'].iloc[0] == 4
        assert combined_df[combined_df['book_title'] == 'Being Mortal']['average_rating'].iloc[0] == 4.5

        # Check if number of favorites is zero for both books
        assert combined_df[combined_df['book_title'] == 'Circe']['number_favorites'].iloc[0] == 0
        assert combined_df[combined_df['book_title'] == 'Being Mortal']['number_favorites'].iloc[0] == 0
    
    def test_analyze_ratings_large_dataset(self, setup_analyzer):
        book_club_db = pd.DataFrame({
            'book_title': ['Educated', 'Sapiens', '1984', 'The Alchemist', 'The Lean Startup', 'To Kill a Mockingbird', 'Sapiens', 'The Lean Startup', 'Educated'],
            'member_name': ['Alice', 'Jose', 'Li Wei', 'Sunita', 'Fatima', 'Akiko', 'Emeka', 'Khaled', 'Alice'],
            'rating': [5, 4.5, 5, 4, 4.5, 4, 4.5, 3.5, 5]
        })

        combined_df = setup_analyzer.analyze_ratings(book_club_db)

        # Check average rating
        assert combined_df[combined_df['book_title'] == 'Educated']['average_rating'].iloc[0] == 5
        assert combined_df[combined_df['book_title'] == 'Sapiens']['average_rating'].iloc[0] == 4.5
        assert combined_df[combined_df['book_title'] == '1984']['average_rating'].iloc[0] == 5
        assert combined_df[combined_df['book_title'] == 'The Alchemist']['average_rating'].iloc[0] == 4
        assert combined_df[combined_df['book_title'] == 'The Lean Startup']['average_rating'].iloc[0] == 4
        assert combined_df[combined_df['book_title'] == 'To Kill a Mockingbird']['average_rating'].iloc[0] == 4

        # Check number of favorites
        assert combined_df[combined_df['book_title'] == 'Educated']['number_favorites'].iloc[0] == 2
        assert combined_df[combined_df['book_title'] == 'Sapiens']['number_favorites'].iloc[0] == 0
        assert combined_df[combined_df['book_title'] == '1984']['number_favorites'].iloc[0] == 1
        assert combined_df[combined_df['book_title'] == 'The Alchemist']['number_favorites'].iloc[0] == 0
        assert combined_df[combined_df['book_title'] == 'The Lean Startup']['number_favorites'].iloc[0] == 0
        assert combined_df[combined_df['book_title'] == 'To Kill a Mockingbird']['number_favorites'].iloc[0] == 0

    def test_analyze_ratings_with_zero_ratings(self, setup_analyzer):
        """Test if function correctly handles books with zero ratings."""
        book_club_db = pd.DataFrame({
            'book_title': ['The Lean Startup', 'The Lean Startup', 'The Alchemist', 'Educated', '1984'],
            'member_name': ['Alice', 'Bob', 'Jose', 'Li Wei', 'Fatima'],
            'rating': [0, 0, 4.5, 5, 5]
        })
        
        combined_df = setup_analyzer.analyze_ratings(book_club_db)

        # Check if average rating is computed correctly for zero ratings
        assert combined_df[combined_df['book_title'] == 'The Lean Startup']['average_rating'].iloc[0] == 0

        # Check if number of favorites is computed correctly for zero ratings
        assert combined_df[combined_df['book_title'] == 'The Lean Startup']['number_favorites'].iloc[0] == 0

        # Check average and number of favorites for other books as well
        assert combined_df[combined_df['book_title'] == 'The Alchemist']['average_rating'].iloc[0] == 4.5
        assert combined_df[combined_df['book_title'] == 'The Alchemist']['number_favorites'].iloc[0] == 0
        assert combined_df[combined_df['book_title'] == 'Educated']['average_rating'].iloc[0] == 5
        assert combined_df[combined_df['book_title'] == 'Educated']['number_favorites'].iloc[0] == 1
        assert combined_df[combined_df['book_title'] == '1984']['average_rating'].iloc[0] == 5
        assert combined_df[combined_df['book_title'] == '1984']['number_favorites'].iloc[0] == 1