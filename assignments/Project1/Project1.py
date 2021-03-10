from typing import Dict, Callable, List

import requests
from bs4 import BeautifulSoup
from pandas import DataFrame

'''
Methods to parse string as a float height.
'''


# parse 0'0"
def parse_qt_height(raw: str) -> float:
    return int(raw[0:raw.index('\'')]) + (float(raw[raw.index('\'') + 1 : -1]) / 12)


# parse 0-0
def parse_ln_height(raw: str) -> float:
    return int(raw[0:raw.index('-')]) + (float(raw[raw.index('-') + 1]) / 12)


'''
List of methods used to parse soup as names and heights from various sites.
'''


def parse_list(soup: BeautifulSoup) -> Dict[str, float]:
    return {row.find("h3").text.strip(): parse_qt_height(row.find("span", {"class": "sidearm-roster-player-height"}).text) for row in soup.find_all("div", {"class": "sidearm-roster-player-pertinents"})}


def parse_table(soup: BeautifulSoup) -> Dict[str, float]:
    return {row.find("td", {"class": "sidearm-table-player-name"}).text.strip(): parse_ln_height(row.find("td", {"class": "height"}).text) for row in soup.find("div", {"data-bind": "if: active_template().id == 2, css: {'sidearm-roster-template-active': active_template().id == 2}"}).find("tbody").find_all("tr")}


'''
Team URLs and required parsing method (above).
'''
urls: Dict[str, List[Callable[[BeautifulSoup], Dict[str, float]]]] = {
    "https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster/2019": parse_list,
    "https://www.brooklyncollegeathletics.com/sports/womens-volleyball/roster/2019": parse_list,
    "https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster": parse_list,
    "https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster": parse_list,
    "https://yorkathletics.com/sports/mens-volleyball/roster": parse_table,
    "https://johnjayathletics.com/sports/womens-volleyball/roster": parse_list,
    "https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster": parse_list,
    "https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster": parse_list,
    "https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster": parse_list,
    "https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster": parse_list,
    "https://yorkathletics.com/sports/mens-swimming-and-diving/roster": parse_table,
    "https://queensknights.com/sports/womens-swimming-and-diving/roster": parse_table
}

mens_swimming: DataFrame
mens_volleyball: DataFrame
womens_swimming: DataFrame
womens_volleyball: DataFrame


def q1() -> None:
    print("1. Scrape data and compile a dataframe of all the names and heights of the players on the men’s swimming team")

    # get urls
    url_set: Dict[str, Callable[[BeautifulSoup], Dict[str, float]]] = {url: v for url, v in urls.items() if "/mens-swimming" in url}

    df: DataFrame = DataFrame()

    # for each url get names and heights then condense into a single dataframe
    global mens_swimming
    for url, method in url_set.items():
        df = df.append(get_heights(url, method))
    df = df.sort_values(by="height")
    mens_swimming = df

    print(df)

    return


def q2() -> None:
    print("2. Scrape data and compile a dataframe of all the names and heights of the players on the women’s swimming team")

    # get urls
    url_set: Dict[str, Callable[[BeautifulSoup], Dict[str, float]]] = {url: v for url, v in urls.items() if "/womens-swimming" in url}

    df: DataFrame = DataFrame()

    # for each url get names and heights then condense into a single dataframe
    global womens_swimming
    for url, method in url_set.items():
        df = df.append(get_heights(url, method))
    df = df.sort_values(by="height")
    womens_swimming = df

    print(df)

    return


def q3() -> None:
    print("3. Scrape data and compile a dataframe of all the names and heights of the players on the men’s volleyball team")

    # get urls
    url_set: Dict[str, Callable[[BeautifulSoup], Dict[str, float]]] = {url: v for url, v in urls.items() if "/mens-volleyball" in url}

    df: DataFrame = DataFrame()

    # for each url get names and heights then condense into a single dataframe
    global mens_volleyball
    for url, method in url_set.items():
        df = df.append(get_heights(url, method))
    df = df.sort_values(by="height")
    mens_volleyball = df

    print(df)

    return


def q4() -> None:
    print("4. Scrape data and compile a dataframe of all the names and heights of the players on the women’s volleyball team")

    # get urls
    url_set: Dict[str, Callable[[BeautifulSoup], Dict[str, float]]] = {url: v for url, v in urls.items() if "/womens-volleyball" in url}

    df: DataFrame = DataFrame()

    # for each url get names and heights then condense into a single dataframe
    global womens_volleyball
    for url, method in url_set.items():
        df = df.append(get_heights(url, method))
    df = df.sort_values(by="height")
    womens_volleyball = df

    print(df)

    return


def get_heights(
        url: str,
        parse: Callable[[BeautifulSoup], Dict[str, float]]) -> DataFrame:
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")
    # for each row in the table, extract the row then extract the name and height to populate a dictionary
    data: Dict[str, float] = parse(soup)

    return DataFrame({"name": data.keys(), "height": data.values()})


def q5() -> None:
    print("5. Find the average height in each of the 4 dataframes (so you should have 4 averages in total)")

    if mens_volleyball is None or womens_volleyball is None or mens_swimming is None or womens_swimming is None:
        print("Please run q1(), q2(), q3(), and q4()")
        return

    print(f"Men's Volleyball Average: {mens_volleyball['height'].mean():.2f} ft.")
    print(f"Men's Swimming Average: {mens_swimming['height'].mean():.2f} ft.")
    print(f"Women's Volleyball Average: {womens_volleyball['height'].mean():.2f} ft.")
    print(f"Women's Swimming Average: {womens_swimming['height'].mean():.2f} ft.")

    return


def q6() -> None:
    print("6. List the names and the heights of the 5 tallest and the 5 shortest swimmers and volleyball players for both the men’s and women’s teams. That is you must have 8 lists in total: tallest men swimmers, tallest men volleyball players, tallest women swimmers, tallest women volleyball players, shortest men swimmers, shortest women volleyball players, shortest women swimmers, shortest women volleyball players,")

    if mens_volleyball is None or womens_volleyball is None or mens_swimming is None or womens_swimming is None:
        print("Please run q1(), q2(), q3(), and q4()")
        return

    print("Men's Volleyball (shortest)"     , mens_volleyball.head(5)  , sep='\n')
    print("Men's Volleyball (tallest)"      , mens_volleyball.tail(5)  , sep='\n')
    print("Men's Swimming (shortest)"       , mens_swimming.head(5)    , sep='\n')
    print("Men's Swimming (tallest)"        , mens_swimming.tail(5)    , sep='\n')
    print("Women's Volleyball (shortest)"   , womens_volleyball.head(5), sep='\n')
    print("Women's Volleyball (tallest)"    , womens_volleyball.tail(5), sep='\n')
    print("Women's Swimming (shortest)"     , womens_swimming.head(5)  , sep='\n')
    print("Women's Swimming (tallest)"      , womens_swimming.tail(5)  , sep='\n')

    return


# run all question methods
if __name__ == "__main__":
    [method() for method in [q1, q2, q3, q4, q5, q6]]
