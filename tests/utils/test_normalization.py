import pytest
import pandas as pd
from utils.normalization import TextNormalizer

@pytest.fixture
def normalizer():
    return TextNormalizer()

class TestTextNormalizer:
    def test_basic_normalization(self, normalizer):
        input_texts = [
            "Circe ",
            " The Hitchhiker's Guide to the Galaxy",
            "Being Mortal",
            "When Breath Becomes Air ",
            " Between the World and Me",
            "Farenheit 451"
        ]

        expected_output = [
            "circe",
            "the hitchhiker's guide to the galaxy",
            "being mortal",
            "when breath becomes air",
            "between the world and me",
            "farenheit 451"
        ]

        assert normalizer.normalize_text(input_texts) == expected_output

    def test_empty_list(self, normalizer):
        assert normalizer.normalize_text([]) == []

    def test_mixed_cases(self, normalizer):
        input_texts = [" CiRCe", "tHE HItchHIker's GuIdE to tHe Galaxy "]
        expected_output = ["circe", "the hitchhiker's guide to the galaxy"]
        assert normalizer.normalize_text(input_texts) == expected_output

    def test_only_spaces(self, normalizer):
        input_texts = [" ", "     "]
        expected_output = ["", ""]
        assert normalizer.normalize_text(input_texts) == expected_output
    
    def test_normalize_db(self, normalizer):
        incorrect_book_club_data = {
            'book_title': [
                "Circe ",
                " The Hitchhiker's Guide to the Galaxy",
                "Being Mortal",
                "When Breath Becomes Air ",
                " Between the World and Me",
                "Farenheit 451"
            ],
            'member_name': [' AliCe ', 'bOB  ', ' JOhn', 'Jane   ', 'ElIzAbeth', '   MARY '],
            'rating': [5, 4.5, 3, 4, 5, 3.5]
        }

        correct_book_club_data = {
            'book_title': [
                "circe",
                "the hitchhiker's guide to the galaxy",
                "being mortal",
                "when breath becomes air",
                "between the world and me",
                "farenheit 451"
            ],
            'member_name': ['alice', 'bob', 'john', 'jane', 'elizabeth', 'mary'],
            'rating': [5, 4.5, 3, 4, 5, 3.5]
        }

        
        df = pd.DataFrame(incorrect_book_club_data)
        normalized_df = pd.DataFrame(correct_book_club_data)

        assert normalizer.normalize_db(df).to_json() == normalized_df.to_json()