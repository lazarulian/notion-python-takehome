import os
from notion_client import Client
import json
import requests

class NotionDatabaseHooks:
    def __init__(self, NOTION_TOKEN):
        self.notion = Client(auth=NOTION_TOKEN)

    def __get_database_entries(self, database_id):
        response = self.notion.databases.query(database_id=database_id)
        data = response

        page_ids = []

        for result in data["results"]:
            if result["object"] == "page":
                page_ids.append(result["id"])
        
        return page_ids

    def clear_database(self, database_id):
        pages_to_archive = self.__get_database_entries(database_id)

        for page_id in pages_to_archive:
            self.notion.pages.update(page_id=page_id, archived=True)
    
    def add_entry(self, database_id, data):
        res = self.notion.pages.create(
            parent={
                "type": "database_id",
                "database_id": database_id
            },
            properties=data
        )
        
        return res
