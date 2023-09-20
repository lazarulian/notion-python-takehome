import pytest
from utils.validation import InputValidator
import pandas as pd

class TestInputValidator:
    @pytest.fixture
    def setup_error_validator(self):
        incorrect_data = {
            'book_title': ['Book 1', 'Book 2', 'Book 3'],
            'member_name': ['Alice', 'Bob', 1234],
            'rating': [5, 4.5, 10]
        }
        df = pd.DataFrame(incorrect_data)
        return InputValidator(df)

    def test_validate_types(self, setup_error_validator):
        with pytest.raises(ValueError, match="The member names are not typed as strings."):
            setup_error_validator.validate_types()

    def test_validate_rating_range(self, setup_error_validator):
        with pytest.raises(ValueError, match="Ratings should be between 0 and 5."):
            setup_error_validator.validate_rating_range()

    def test_validate_csv(self, setup_error_validator):
        with pytest.raises(ValueError) as error:
            setup_error_validator.validate_csv()
        assert str(error.value) in ["The member names are not typed as strings.", "Ratings should be between 0 and 5."]

    
    @pytest.fixture
    def setup_correct_validator(self):
        incorrect_data = {
            'book_title': ['Book 1', 'Book 2', 'Book 3'],
            'member_name': ['Alice', 'Bob', 'John'],
            'rating': [5, 4.5, 3]
        }
        df = pd.DataFrame(incorrect_data)
        return InputValidator(df)
    
    def test_validate_csv(self, setup_correct_validator):
        assert setup_correct_validator.validate_csv() == True