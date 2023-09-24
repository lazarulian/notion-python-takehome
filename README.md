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

I think the largest roadblock that I faced when working on the project was figuring out the schema for using the Notion API. I decided to use the Python SDK because I thought it would be fun and usually I do these types of projects using TypeScript & Express but was surprised that the API documentation didn't have many code snippets supported for Python. After a while, I realized the SDKs were almost identical but it would have been nice to have some sort of examples/quickstarts for each SDK to get started with. 

To figure out how to get the API working properly, I opened an environment following some starter code that the Python SDK did have and started playing with how responses looked in JS and plugging in that data when calling other endpoints. For example, when figuring out how to create pages in a database, I first queried the database, figured out how the properties were displayed on the response, and then modeled the API call to mirror the schema of the properties. 

> Do you have any suggestions for improving the API documentation to make it clearer or easier to use?

I think the API documentation is a great resource right now but could use some changes to the UI.
- Put the code blocks inline because most of the responses and code are cut off for laptop-sized devices
- Add more quickstart guides for all of the SDK types

## Resources Used
- [Notion Developer Docs](https://developers.notion.com/)
- [How to work with the Notion API in Python](https://www.python-engineer.com/posts/notion-api-python/)
- [Pytest Docs](https://docs.pytest.org/en/7.1.x/contents.html)
