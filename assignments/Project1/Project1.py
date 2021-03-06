from typing import Dict, Callable, List

import requests
from bs4 import BeautifulSoup, Tag
from pandas import DataFrame

'''
Methods to parse string as a float height.
'''

# parse 0'0"
parse_qt_height: Callable[[str], float] = lambda x: int(x[0:x.index('\'')]) + (float(x[x.index['\''] + 1 : -1]) / 12)
# parse 0-0
parse_ln_height: Callable[[str], float] = lambda x: int(x[0:x.index['-']]) + (float(x[x.index['-'] + 1]) / 12)

'''
List of methods used to parse soup to names and heights.
'''

# <row,name,height,parse_height>
parse_bkln: List[Callable] = [None, None, None, parse_qt_height]
parse_brch: List[Callable] = [None, None, None, parse_qt_height]
parse_york: List[Callable] = [None, None, None, parse_ln_height]
parse_jjay: List[Callable] = [None, None, None, parse_qt_height]
parse_qc: List[Callable]   = [None, None, None, parse_ln_height]

'''
Team URLs and required parsing method (above).
'''
urls: Dict[str, List[Callable]] = {
    "https://www.brooklyncollegeathletics.com/sports/mens-volleyball/roster/2019": parse_bkln,
    "https://www.brooklyncollegeathletics.com/sports/womens-volleyball/roster/2019": parse_bkln,
    "https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster": parse_brch,
    "https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster": parse_brch,
    "https://yorkathletics.com/sports/mens-volleyball/roster": parse_york,
    "https://johnjayathletics.com/sports/womens-volleyball/roster": parse_jjay,
    "https://www.brooklyncollegeathletics.com/sports/mens-swimming-and-diving/roster": parse_bkln,
    "https://www.brooklyncollegeathletics.com/sports/womens-swimming-and-diving/roster": parse_bkln,
    "https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster": parse_brch,
    "https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster": parse_brch,
    "https://yorkathletics.com/sports/mens-swimming-and-diving/roster": parse_york,
    "https://queensknights.com/sports/womens-swimming-and-diving/roster": parse_qc
}

mens_swimming: DataFrame
mens_volleyball: DataFrame
womens_swimming: DataFrame
womens_volleyball: DataFrame


def q1() -> None:
    print("1. Scrape data and compile a dataframe of all the names and heights of the players on the men’s swimming team")

    urlset: Dict[str, List[Callable]] = {url: v for url, v in urls.items() if "mens-swimming" in url}

    df: DataFrame = DataFrame()

    # for each url run associated methods and condense into a single dataframe
    [df.append(get_heights(url, method[0], method[1], method[2], method[3])) for url, method in urlset.items()]

    print(df)

    return


def q2() -> None:
    print("2. Scrape data and compile a dataframe of all the names and heights of the players on the women’s swimming team")

    urlset: Dict[str, List[Callable]] = {url: v for url, v in urls.items() if "womens-swimming" in url}

    df: DataFrame = DataFrame()

    # for each url run associated methods and condense into a single dataframe
    [df.append(get_heights(url, method[0], method[1], method[2], method[3])) for url, method in urlset.items()]

    print(df)

    return


def q3() -> None:
    print("3. Scrape data and compile a dataframe of all the names and heights of the players on the men’s volleyball team")

    urlset: Dict[str, List[Callable]] = {url: v for url, v in urls.items() if "mens-volleyball" in url}

    df: DataFrame = DataFrame()

    # for each url run associated methods and condense into a single dataframe
    [df.append(get_heights(url, method[0], method[1], method[2], method[3])) for url, method in urlset.items()]

    print(df)

    return


def q4() -> None:
    print("4. Scrape data and compile a dataframe of all the names and heights of the players on the women’s volleyball team")

    urlset: Dict[str, List[Callable]] = {url: v for url, v in urls.items() if "womens-volleyball" in url}

    df: DataFrame = DataFrame()

    # for each url run associated methods and condense into a single dataframe
    [df.append(get_heights(url, method[0], method[1], method[2], method[3])) for url, method in urlset.items()]

    print(df)

    return


def get_heights(
        url: str,
        soup_row: Callable[[BeautifulSoup], Tag],
        soup_name: Callable[[Tag], str],
        soup_height: Callable[[Tag], str],
        parse_height: Callable[[str], float]) -> DataFrame:
    """
    Parses heights from a site into a dataframe.

    :param url: site url
    :param soup_row: method that retrieves person rows from soup
    :param soup_name: method that retrieves name from person row
    :param soup_height: method that retrieves height from person row
    :param parse_height: method that parses height syntax
    :return:
    """
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")
    # for each row in the table, extract the name and height to populate a dictionary
    data: Dict[str, float] = {soup_name(tag): parse_height(soup_height(tag)) for tag in soup_row(soup)}

    return DataFrame(data)


def q5() -> None:
    print("5. Find the average height in each of the 4 dataframes (so you should have 4 averages in total)")

    if not mens_volleyball or not womens_volleyball or not mens_swimming or not womens_swimming:
        print("Please run q1(), q2(), q3(), and q4()")
        return

    return


def q6() -> None:
    print("6. List the names and the heights of the 5 tallest and the 5 shortest swimmers and volleyball players for both the men’s and women’s teams. That is you must have 8 lists in total: tallest men swimmers, tallest men volleyball players, tallest women swimmers, tallest women volleyball players, shortest men swimmers, shortest women volleyball players, shortest women swimmers, shortest women volleyball players,")

    if not mens_volleyball or not womens_volleyball or not mens_swimming or not womens_swimming:
        print("Please run q1(), q2(), q3(), and q4()")
        return

    return


# run all question methods
if __name__ == "__main__":
    [method() for method in [q1, q2, q3, q4, q5, q6]]
