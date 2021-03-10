from typing import List

import requests
from bs4 import BeautifulSoup, Tag
from pandas import DataFrame


def main() -> None:
    # read site
    url: str = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population"
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")

    [s.extract() for s in soup.find_all("sup", {"class": "reference"})]

    # get table body
    table: Tag = soup.find("table", {"class": "wikitable sortable", "style": "width:100%; text-align:center;"})

    # populate dataset
    data: List[List[str or float]] = []
    for row in table.find("tbody").find_all("tr"):  # for each row
        row: Tag
        if row.has_attr("class") and row["class"][0] == "sortbottom" or row.find("th"):  # exclude header and footer rows
            continue
        cols: List[str or float] = []
        for col in row.find_all("td"):  # for each col
            raw: str = col.text.strip()
            try:  # if string can be expressed as float then cast, otherwise save raw string
                cols.append(float(raw.strip("+%*").replace(',', '').replace("–", '-')))
            except ValueError:
                cols.append(raw)
        data.append(cols)

    # export as csv DataFrame
    df: DataFrame = DataFrame(data, columns=["Current Rank", "2010 Rank", "State/Territory", "2020 Pop.", "2010 Pop.", "% Pop. Change", "Net Change", "House Seats", "Percent House", "Pop. / Electoral Vote", "2020 Pop. / Seat", "2010 Pop. / Seat", "2020 % US Pop.", "2010 % US Pop.", "% US Pop. Change", "% Electoral College"])
    df.to_csv("us_pop.csv")

    # describe
    print(df[["2020 Pop.", "2020 % US Pop."]].describe())

    return


if __name__ == "__main__":
    main()
