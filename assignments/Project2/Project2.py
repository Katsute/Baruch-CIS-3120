import time
import urllib.parse
from typing import Dict, List

from bs4 import BeautifulSoup, Tag
import pandas as pd
import requests


# API: https://docs.coincap.io/
# API requires no token
# Table: https://coinmarketcap.com/all/views/all/
def main() -> None:
    # Table scrape
    url: str = "https://coinmarketcap.com/all/views/all"
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")

    i: int = 0
    limit: int = 50  # max to process
    tableset: List[List[str or float]] = []
    for row in soup.find_all("tr", {"class": "cmc-table-row", "style": "display:table-row"}):  # for each row
        i += 1
        if i > limit: break

        row: Tag
        cols: List[str or float] = []
        for col in row.find_all("td"):  # for each col
            raw: str = col.text.strip()
            try:  # if string can be expressed as float then cast, otherwise save raw string
                cols.append(float(raw.strip("+%*").replace(',', '').replace("–", '-')))
            except ValueError:
                cols.append(raw)
        tableset.append(cols)

    tbl_df: pd.DataFrame = pd.DataFrame(tableset, columns=["Rank", "Name", "Symbol", "Market Cap", "Price", "Circulating Supply", "Volume(24h)", "% 1h", "% 24h", "% 7d", "..."])

    # API
    base_url: str = "https://api.coincap.io/v2"
    dataset: Dict[str, Dict[str, float or str]] = {}

    i: int = 0
    size: int = len(tbl_df["Symbol"])
    for c in tbl_df["Symbol"]:
        i += 1
        print(f"Processing {i}/{size}")
        data: any = request(base_url, "assets/", search=c)["data"][0]
        dataset[c] = {
            "symbol": data["symbol"],
            "supply": float(data["supply"] or 0),
            "maxSupply": float(data["maxSupply"] or 0),
            "marketCapUsd": float(data["marketCapUsd"] or 0),
            "volumeUsd24Hr": float(data["volumeUsd24Hr"] or 0),
            "priceUsd": float(data["priceUsd"] or 0)
        }
        time.sleep(1)  # prevent rate limit

    api_df: pd.DataFrame = pd.DataFrame(dataset)

    # merge df
    df: pd.DataFrame = pd.merge(tbl_df, api_df, on=["Symbol", "symbol"])
    print(df)

    df.to_csv("crypto.csv")

    return


def request(base_url: str, path: str, **kwargs: Dict[str, any]) -> any:
    url: str = base_url + '/' + path
    first: bool = True
    for k, v in kwargs.items():  # query parameters
        url += '?' if first else '&'
        first = False
        url += f"{urllib.parse.quote_plus(k)}={urllib.parse.quote_plus(v)}"

    response: requests.Response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    main()
