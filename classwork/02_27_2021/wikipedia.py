from typing import List

import requests
from bs4 import BeautifulSoup, Tag

url: str = "https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population"

soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")

table: Tag = soup.find("table", class_="wikitable sortable")

grid: List[List[str]] = []

for row in table.find_all("tr"):
    cells: List[Tag] = row.findAll("td")

    if len(cells) > 0:
        for i in range(len(cells)):
            if i+1 > len(grid):
                grid.append([])

            grid[i].append(cells[i].text.rstrip())

print(grid)
