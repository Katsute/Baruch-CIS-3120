# TOC

- [Requests](#requests)
- [Scraping](#scraping)
- [Pandas](#pandas)
  - [Concat Dataframes](#concat-dataframes)
  - [Index](#index)
- [Numpy](#numpy)

Requires [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)

## Requests

```python
import requests
from requests import Response

url = "https://en.wikipedia.org/wiki/Pet"
r = requests.get(url)
html = r.text
```

## Scraping

```python
import requests
from bs4 import BeautifulSoup, Tag

url = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

soup = BeautifulSoup(requests.get(url).content, "html.parser")
table = soup.find("table", class_="wikitable sortable")
```

## Pandas

```python
import pandas as pd

roster = pd.DataFrame(dictionary)

roster.head(1)  # first
roster.tail(1)  # last
roster.shape  # shape (x, y) len
roster.describe()  # describe: summary of count, mean, std, min, quartiles, max
roster.T  # transpose: swap axes
roster.sort_values(by="GPA")  # sort
roster[1:3]  # slicing
roster[roster['GPA'] > 3.5]  # filter
```

### Concat Dataframes

```python
pd.concat([df1, df2])
```

### Index

```python
df.set_index("Name").loc["Value"]  # select row?
df.iloc["Value"]  # select column?
df.index["Index", "Value"]  # index?

mask = df["Key"] == "Value"
df[mask]  # mask
```

## Numpy

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

np.zeros([3, 4], dtype=int)  # of zeroes
np.ones([3, 4], dtype=int)  # of ones
np.random.randint(0, 20)  # of rand
```