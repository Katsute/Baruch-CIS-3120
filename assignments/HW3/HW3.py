import urllib.parse
from typing import Dict, List

import pandas as pd
import requests


# API: https://docs.coincap.io/
# API requires no token
def main() -> None:
    base_url: str = "https://api.coincap.io/v2"

    currencies: List[str] = ["bitcoin", "bitcoin-cash", "binance-coin", "dogecoin", "ethereum", "ethereum-classic", "litecoin", "monero", "stellar", "tether"]

    dataset: Dict[str, Dict[str, float]] = {}

    for c in currencies:
        data: any = request(base_url, "assets/" + c)["data"]
        dataset[c] = {
            "supply":        float(data["supply"] or 0),
            "maxSupply":     float(data["maxSupply"] or 0),
            "marketCapUsd":  float(data["marketCapUsd"] or 0),
            "volumeUsd24Hr": float(data["volumeUsd24Hr"] or 0),
            "priceUsd":      float(data["priceUsd"] or 0)
        }

    pd.options.display.width = None
    pd.options.display.float_format = lambda x: '%.2f' % x
    df: pd.DataFrame = pd.DataFrame(dataset)
    print(df)

    df.to_csv("crypto.csv")

    print(df.transpose().describe())

    return


def request(base_url: str, path: str) -> any:
    url: str = base_url + '/' + path
    response: requests.Response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    main()
