import sys
import urllib.parse
from typing import Dict, Any

import requests

def main(*args: [Any]) -> None:
    if not args[0]:
        return
    return


def request(path: str, **kwargs: Dict[str, Any]) -> Any:
    url: str = path
    first: bool = True
    for k, v in kwargs:
        url += '?' if first else '&'
        first = False
        url += f"{urllib.parse.quote_plus(k)}={urllib.parse.quote_plus(v)}"

    response: requests.Response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    main(sys.argv[1:])