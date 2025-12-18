# mini-pandas

A lightweight CSV data manipulation library inspired by pandas.

## Features
- Read/write CSV files
- Basic data analysis (null counts, statistics)
- Type handling (int, float, string)

## Usage
```python
from DataFrame.dataframe import Dataframe

df = Dataframe.read_csv('titanic.csv', 'titanic_dtype.csv')
print(df.count_nulls())
df.to_csv('output.csv')
```

## Run
```bash
python -m DataFrame.dataframe
```

