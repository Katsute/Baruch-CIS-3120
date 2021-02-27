from typing import List

import requests
from bs4 import BeautifulSoup, Tag

url: str = "https://avinashjairam.github.io/tableExample1.html"

soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")

months: List[str] = []
savings: List[str] = []

table: Tag = soup.find("table")

for row in table.find_all("tr"):
    cells: List[Tag] = row.findAll("td")
    if len(cells) > 0:
        months.append(cells[0].text)
        savings.append(cells[1].text[1:])

print(months)
print(savings)

# dataframe

import pandas as pd

df = pd.DataFrame()
df['month'] = months
df['savings'] = savings

df.to_csv("df.csv")
