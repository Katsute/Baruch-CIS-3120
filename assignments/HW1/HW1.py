import requests
from bs4 import BeautifulSoup

m_sw_ht: list[float]
m_vb_ht: list[float]
f_sw_ht: list[float]
f_vb_ht: list[float]


def q1() -> None:
    print("1. Scrape the heights of all the players on the men’s swimming team and find the average.")
    # get height & average using below functions
    heights: list[float] = get_heights("https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster")
    avg: float = average(heights)

    print(f"Average height is {avg:.2f} ft.")

    # set global, required for last 3 questions
    global m_sw_ht
    m_sw_ht = heights

    return


def q2() -> None:
    print("2. Scrape the heights of all the players on the men’s volleyball team and find the average.")
    # get height & average using below functions
    heights: list[float] = get_heights("https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster")
    avg: float = average(heights)

    print(f"Average height is {avg:.2f} ft.")

    # set global, required for last 3 questions
    global m_vb_ht
    m_vb_ht = heights

    return


def q3() -> None:
    print("3. Scrape the heights of all the players on the women’s swimming team and find the average.")
    # get height & average using below functions
    heights: list[float] = get_heights("https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster")
    avg: float = average(heights)

    print(f"Average height is {avg:.2f} ft.")

    # set global, required for last 3 questions
    global f_sw_ht
    f_sw_ht = heights

    return


def q4() -> None:
    print("4. Scrape the heights of all the players on the women’s volleyball team and find the average.")
    # get height & average using below functions
    heights: list[float] = get_heights("https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster")
    avg: float = average(heights)

    print(f"Average height is {avg:.2f} ft.")

    # set global, required for last 3 questions
    global f_vb_ht
    f_vb_ht = heights

    return


def get_heights(url: str) -> list[float]:
    # read raw site
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).content, "html.parser")
    # pull heights from span.sidearm-roster-player-height and append to list
    heights: list[float] = [parse_height(tag.text) for tag in soup.find_all("span", {"class": "sidearm-roster-player-height"})]

    return heights


# parse 0'0"
def parse_height(string: str) -> float:
    return int(string[0:string.index('\'')]) + (float(string[string.index('\'') + 1:-1]) / 12)


def average(array: list[float] or list[list[float]]) -> float:
    if type(array[0]) is float:  # average for 1 dimensional list
        return sum(array) / len(array)
    else:  # average for list of lists
        arr2 = []
        for arr in array:  # condense into single list
            arr: list[float]
            arr2.extend(arr)
        return average(arr2)


def q5() -> None:
    print("5. Compare the averages between the two men’s teams. Write a few lines about your findings.")

    # required variables
    if m_sw_ht is None or m_vb_ht is None:
        print("NullPointerException: Men's averages not found, please run q1() and q2() first.")
        return

    diff: float = average(m_sw_ht) - average(m_vb_ht)
    print(f"Diff: {diff:.2f} ft.")

    return


def q6() -> None:
    print("6. Compare the averages between the two women’s teams. Write a few lines about your findings")

    # required variables
    if f_sw_ht is None or f_vb_ht is None:
        print("NullPointerException: Women's averages not found, please run q3() and q4() first.")
        return

    diff: float = average(f_sw_ht) - average(f_vb_ht)
    print(f"Diff: {diff:.2f} ft.")

    return


def q7() -> None:
    print(
        "7. Are you able to determine whether, in general, if the average swimmer is taller than the average volleyball player? Write a few lines about your findings")

    # required variables
    if m_sw_ht is None or m_vb_ht is None or f_sw_ht is None or f_vb_ht is None:
        print("NullPointerException: Averages not found, please run q1(), q2(), q3(), and q4() first.")
        return

    diff: float = average([m_sw_ht, f_sw_ht]) - average([m_vb_ht, f_vb_ht])
    print(f"Diff: {diff:.2f} ft.")

    return


# run all q methods
if __name__ == '__main__':
    for func in [q1, q2, q3, q4, q5, q6, q7]:
        func()

