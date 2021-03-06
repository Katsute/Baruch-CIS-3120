from typing import List, Dict

import pandas as pd

dictionary: Dict[str, List[str or float]] = {
    "Name": ["Bob", "Alice", "Joe", "Mike", "Lisa"],
    "Major": ["Accounting", "Finance", "Chemistry", "Art", "Engineering"],
    "GPA": [3.5, 3.8, 3.2, 3.7, 4.0],
    "Age": [22, 23, 31, 48, 25]
}

roster = pd.DataFrame(dictionary)

print(roster)

print(roster.head(1))  # first
print(roster.tail(1))  # last

print(roster.shape)  # shape (x, y) len
print(roster.describe())  # describe: summary of count, mean, std, min, quartiles, max
print(roster.T)  # transpose: swap axes

print(roster.sort_values(by="GPA"))  # sort

print(roster[1:3])  # slicing

print(roster[roster['GPA'] > 3.5])  # filter
