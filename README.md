# book-club-analyzer

A simple ratings analyzer that intakes csv book club data and outputs some analysis into a notion table of choice. 

## Getting Started
### Requirements
- [Python](https://www.python.org/downloads/)
- [Notion Account](https://www.notion.so/)
- [Notion Integration Key](https://developers.notion.com/docs/create-a-notion-integration)

### Running the Script

1. Clone this repository.

```bash
git clone https://github.com/lazarulian/notion-python-takehome.git
```

2. Install the necessary python dependencies.

```bash
pip install -r requirements.txt
```

3. Run the script.

```bash
python app.py
```

At this stage, when prompted input:
- the path to your CSV file with the ratings
- your database ID
- your notion integration key

## Short Answer Questions
> Was there anything you got stuck on, and if so what did you do to resolve it?

I think the largest roadblock I faced was learning how to organize the project to write clean code that matches all of the requirements. One of the most frustrating parts of building something is to organize the project in a specific way and then have to change the structure later on when realizing something won't work in the current setup. In this case, deciding how to split up all of the utility functions, and service functions was a challenge for me when taking into account that I would need to expand the program in the future to add additional functionality. 

To learn how to structure the project, I looked into how other open-source projects organized their own repositories and traced through the imports to see why they made those choices. I also looked into Refactoring.Guru to learn some design patterns that would help make the code intentional and modular for future contributions.

> Do you have any suggestions for improving the API documentation to make it clearer or easier to use?

I think the API documentation is a great resource right now but could use some changes to the UI.
- Put the code blocks & responses inline because most of the responses and code are cut off for laptop-sized devices
- Add more quickstart guides for all of the SDK types, rather than just JavaScript

## Resources Used
- [Notion Developer Docs](https://developers.notion.com/)
- [How to work with the Notion API in Python](https://www.python-engineer.com/posts/notion-api-python/)
- [Pytest Docs](https://docs.pytest.org/en/7.1.x/contents.html)
- [Design Patterns](https://refactoring.guru/design-patterns)

## Open Source Libraries Used
- Pytest for tests
- Requests for networking
- Pandas for data manipulation
- Notion SDK for API calls
