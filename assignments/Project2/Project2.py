import time
import urllib.parse
from typing import Dict, List

from bs4 import BeautifulSoup, Tag
import pandas as pd
import requests


# API: https://docs.coincap.io/
# API requires no token
# Table: https://coinmarketcap.com/
def main() -> None:
    # Table scrape
    url: str = "https://coinmarketcap.com/"
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")

    i: int = 0
    limit: int = 50  # max to process
    tableset: List[List[str or float]] = []
    for row in soup.find("table", {"class": "cmc-table"}).find("tbody").find_all("tr"):  # for each row
        i += 1
        if i > limit: break

        row: Tag
        cols: List[str or float] = [
            (row.find("p", {"class": "coin-item-symbol"}) or row.find("span", {"class": "crypto-symbol"})).text.strip()
        ]
        for col in row.find_all("td"):  # for each col
            raw: str = col.text.strip()
            try:  # if string can be expressed as float then cast, otherwise save raw string
                cols.append(float(raw.strip("+%*").replace(',', '').replace("–", '-')))
            except ValueError:
                cols.append(raw)

        tableset.append(cols)

    tbl_df: pd.DataFrame = pd.DataFrame(tableset, columns=["symbol", "?", "#", "Name", "Price", "24Hr%", "7d%", "Market Cap", "Volume", "Supply", "7d", "??"])

    # API
    base_url: str = "https://api.coincap.io/v2"
    dataset: Dict[str, Dict[str, float or str]] = {}

    i: int = 0
    delay: int = 5
    size: int = len(tbl_df["symbol"])
    print("API requests will be delayed to prevent rate limit")
    for c in tbl_df["symbol"]:
        i += 1
        print(f"Processing {i}/{size} :: {base_url}/assets?search={c} :: {(size-i)*delay}s remaining")
        data: List[any] = request(base_url, "assets/", search=c)["data"]
        first: Dict[str, str] = data[0] if len(data) > 0 else {}

        dataset[c] = {
            "symbol"        : first.get("symbol", c),
            "supply"        : float(first.get("supply", '0')),
            "maxSupply"     : float(first.get("maxSupply", '0')),
            "marketCapUsd"  : float(first.get("marketCapUsd", '0')),
            "volumeUsd24Hr" : float(first.get("volumeUsd24Hr", '0')),
            "priceUsd"      : float(first.get("priceUsd", '0'))
        }
        time.sleep(delay)  # prevent rate limit

    api_df: pd.DataFrame = pd.DataFrame(dataset)

    # merge df
    df: pd.DataFrame = pd.merge(tbl_df, api_df.transpose(), on="symbol")
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
