# Pandas Cheat Sheet

## Import

```python
import pandas as pd
```

## Creating DataFrames

```python
# from dictionary
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['NY', 'LA', 'SF']
})

# from list of dicts
data = [{'a': 1, 'b': 2}, {'a': 3, 'b': 4}]
df = pd.DataFrame(data)

# from numpy array
import numpy as np
df = pd.DataFrame(np.random.rand(3, 3), columns=['A', 'B', 'C'])
```

## Reading Files

```python
pd.read_csv('data.csv')           # CSV file
pd.read_excel('data.xlsx')        # Excel file
pd.read_json('data.json')         # JSON file
pd.read_sql(query, connection)    # SQL query
pd.read_html('url')               # HTML tables
```

## Basic Properties

```python
df.head()          # first 5 rows
df.tail()          # last 5 rows
df.shape           # (rows, cols)
df.columns         # column names
df.dtypes          # data types
df.info()          # summary
df.describe()      # stats summary
df.values          # numpy array
df.index           # row indices
```

## Selecting Data

```python
df['Name']                # single column (Series)
df[['Name', 'Age']]       # multiple columns
df[0:3]                   # rows by slice
df.loc[0]                 # row by label
df.loc[0:2, 'Name':'Age'] # rows & cols by label
df.iloc[0]                # row by position
df.iloc[0:2, 0:2]         # rows & cols by position
df.at[0, 'Name']          # single value by label
df.iat[0, 0]              # single value by position
```

## Filtering

```python
df[df['Age'] > 25]                    # filter rows
df[df['City'].isin(['NY', 'LA'])]     # filter with list
df.query('Age > 25 and City == "NY"') # query string
df[df['Name'].str.contains('Ali')]    # string filter
df[(df['Age'] > 25) & (df['City'] == 'NY')]  # multiple conditions
df[df['Age'].between(25, 35)]         # between range
df[df['Name'].isnull()]               # null values
df[df['Name'].notnull()]              # non-null values
```

## Adding & Removing Columns

```python
df['Score'] = [90, 85, 88]            # add column
df['Double Age'] = df['Age'] * 2      # derived column
df.insert(1, 'New', [1, 2, 3])        # insert at position
df.drop('Score', axis=1, inplace=True)  # remove column
df.pop('Score')                        # remove & return column
```

## Adding & Removing Rows

```python
new_row = pd.DataFrame({'Name': ['Dave'], 'Age': [40], 'City': ['Boston']})
df = pd.concat([df, new_row], ignore_index=True)  # add row

df.drop(0, inplace=True)              # remove row by index
df.drop(df[df['Age'] < 30].index, inplace=True)  # remove by condition
```

## Handling Missing Values

```python
df.isnull()              # check nulls
df.isnull().sum()        # count nulls per column
df.dropna()              # drop rows with nulls
df.dropna(subset=['Age']) # drop nulls in specific col
df.fillna(0)             # fill with value
df.fillna(df.mean())     # fill with mean
df.fillna(method='ffill') # forward fill
df.fillna(method='bfill') # backward fill
df.interpolate()         # interpolate values
```

## Sorting

```python
df.sort_values('Age')               # sort by column
df.sort_values('Age', ascending=False)  # descending
df.sort_values(['City', 'Age'])     # sort by multiple
df.sort_index()                     # sort by index
df.sort_values('Age', na_position='last')  # nulls last
```

## Grouping & Aggregation

```python
df.groupby('City')                  # group by column
df.groupby('City')['Age'].mean()    # group + aggregate
df.groupby('City').agg({'Age': 'mean', 'Score': 'max'})
df.groupby('City').agg(
    avg_age=('Age', 'mean'),
    total=('Score', 'sum')
)
df.groupby('City').size()           # count per group
df.groupby('City').count()          # count non-null
```

## Merging & Joining

```python
pd.merge(df1, df2, on='Name')                # inner join
pd.merge(df1, df2, on='Name', how='left')    # left join
pd.merge(df1, df2, on='Name', how='right')   # right join
pd.merge(df1, df2, on='Name', how='outer')   # full join
pd.merge(df1, df2, left_on='L', right_on='R') # different keys

pd.concat([df1, df2])              # stack vertically
pd.concat([df1, df2], axis=1)      # stack horizontally
```

## Applying Functions

```python
df['Age'].apply(lambda x: x + 1)       # apply to column
df.apply(lambda x: x.max() - x.min())  # apply to each col
df.applymap(lambda x: x * 2)           # apply to entire df
df['Name'].map({'Alice': 'A', 'Bob': 'B'})  # map values
df['Name'].replace({'Alice': 'A'})      # replace values
```

## Pivot Tables

```python
pd.pivot_table(df, values='Score', index='City', columns='Name')
pd.pivot_table(df, values='Score', index='City', aggfunc='mean')
pd.pivot_table(df, values='Score', index='City', aggfunc=['mean', 'max'])
```

## String Operations

```python
df['Name'].str.lower()        # lowercase
df['Name'].str.upper()        # uppercase
df['Name'].str.strip()        # remove whitespace
df['Name'].str.contains('li') # contains
df['Name'].str.replace('a', '@')  # replace
df['Name'].str.split(' ')     # split
df['Name'].str.len()          # length
```

## Exporting Data

```python
df.to_csv('output.csv', index=False)     # to CSV
df.to_excel('output.xlsx', index=False)  # to Excel
df.to_json('output.json')                # to JSON
df.to_sql('table_name', connection)      # to SQL
df.to_html('output.html')               # to HTML
```

## Useful Functions

```python
df.rename(columns={'Old': 'New'})    # rename columns
df.reset_index(drop=True)            # reset index
df.set_index('Name')                 # set column as index
df.duplicated()                      # check duplicates
df.drop_duplicates()                 # remove duplicates
df.nunique()                         # unique counts per col
df['Age'].value_counts()             # value counts
df.sample(frac=0.5)                  # random sample 50%
df.clip(lower=0, upper=100)          # clip values
df.rank()                            # rank values
df.corr()                            # correlation matrix
```

## Chaining Operations

```python
result = (df
    .query('Age > 25')
    .groupby('City')
    .agg(avg_age=('Age', 'mean'))
    .sort_values('avg_age', ascending=False)
    .reset_index()
)
```
