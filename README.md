# notion-python-takehome

Book ratings aggregator for notion!

## App Design

### Utility Features

1. **Import**

- Imports CSV to dataframe

2. **Validation**

- Ensures CSV is a well formatted csv with the same 3 column headings in the same order
- Ensure ratings are between 0 to 5 stars, inclusive

3. **Normalization**

- Remove extra spacing from names
- Lowercase all book titles

4. **Aggregation**

- Aggregate average rating, and number of favorites
- Aggregate other useful metaData for future use
- If there are multiple ratings for the same member and book, we should only use the last one.

### Output

- Book Name
- average rating from all members
- number of favorites
