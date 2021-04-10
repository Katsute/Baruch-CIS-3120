import pandas as pd

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

# vertical merge
merge_df = pd.concat([roster1_df, roster2_df], axis=1, ignore_index=True)  # ignore dupe indexes

# left join - use left records ONLY
left = pd.merge(roster1_df, roster2_df, how="left", on=["Name"])  # merge where 'on' column matches
# right join - use right records ONLY
right = pd.merge(roster1_df, roster2_df, how="right", on=["Name"])
# outer join - standard merge, include all records
outer = pd.merge(roster1_df, roster2_df, how="outer", on=["Name"])
# inner join - use matching records ONLY
inner = pd.merge(roster1_df, roster2_df, how="inner", on=["Name"])

# remove NaN
inner.dropna(inplace=True)  # in place means modify df instead of creating new one

# replace NaN
inner[["Name"]] = inner[["Name"]].fillna('nil')
