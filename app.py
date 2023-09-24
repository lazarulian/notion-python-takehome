from utils.ratings import BookClubAggregator
from service.notion_api_hooks import NotionDatabaseHooks
import pandas as pd

if __name__ == "__main__":
    print("\nIntializing Book Club Analyzer 🧘\n")
    
    print("\nPlease input the filepath for your csv file 🗂️")
    FILE_PATH = input()

    print("\nPlease input your database id number 🔢")
    DB_ID = input()

    print("\nPlease input your notion integration key 🔢")
    NOTION_TOKEN = input()
    
    analysis_runner = BookClubAggregator(FILE_PATH)
    ratings = analysis_runner.get_analyzed_ratings()

    print("\nSuccessfully analyzed your data, sending to notion 🔎")
    
    # Initialize Notion Worker
    database_agent = NotionDatabaseHooks(NOTION_TOKEN)

    # Clear Notion Database
    database_agent.clear_database(DB_ID)

    # Update Database
    for book_title, average_rating, number_favorites in zip(ratings['book_title'], ratings['average_rating'], ratings['number_favorites']):
        average_rating = str(average_rating)
        number_favorites = str(number_favorites)
        data = {
            "Book Name": {"title": [{"text": {"content": book_title}}]},
            "Average Rating": {"rich_text": [{"text": {"content": average_rating}}]},
            "Number of Favorites": {"rich_text": [{"text": {"content": number_favorites}}]}
        }

        database_agent.add_entry(DB_ID, data)

    print("\n✅ Success! Successfully updated your database with the data.\n")