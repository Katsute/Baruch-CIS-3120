import pandas as pd

# merge dataframe
roster1 = {"Name": ["Bob", "Alice", "Joe", "Mike", "Lisa", "Alan", "Eli", "Mark", "Liz", "Jane"],
           "Major": ["Accounting", "Finance", "Chemistry", "Art", "Engineering", "Biology", "Physics", "History", "Art",
                     "Engineering"],
           "GPA": [3.5, 3.8, 3.2, 3.7, 4.0, 3.5, 3.8, 3.2, 3.1, 3.0],
           "Age": [22, 23, 31, 40, 25, 22, 33, 31, 27, 55]
           }

roster1_df = pd.DataFrame(roster1)

roster2 = {"Name": ["Bob", "Alice", "Joe", "Mike", "Lisa", "Alan", "Eli", "Mark", "Liz", "Jane"],
           "Major": ["Accounting", "Finance", "Chemistry", "Art", "Engineering", "Biology", "Physics", "History", "Art",
                     "Engineering"],
           "GPA": [3.5, 3.8, 3.2, 3.7, 4.0, 3.5, 3.8, 3.2, 3.1, 3.0],
           "Age": [22, 23, 31, 40, 25, 22, 33, 31, 27, 55]
           }

roster2_df = pd.DataFrame(roster2)

roster_df = pd.concat([roster1_df, roster2_df])

print(roster_df)
print('-')
print(roster2_df.set_index("Name").loc["Alan"])  # select row?
print('-')
print(roster2_df.iloc["Engineering"])  # select column?
print('-')
print(roster2_df.index["Alan", "Engineering"])  # index?

mask = roster1_df["Major"] == "Art"
print(roster1_df[mask])  # mask
