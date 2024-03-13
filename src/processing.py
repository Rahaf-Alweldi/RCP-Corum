#!/usr/bin/env python3
# you should chmod this file before using run.py --> chmod +x processing.py

import pandas as pd

data = pd.read_csv('../data/Corum_timestamp.csv')

# Dropping the empty columns
columns_to_drop = ['type', 'year_introduced', 'style', 'case_shape',
                   'case_finish', 'caseback', 'lug_to_lug', 'bezel_material',
                   'bezel_color', 'crystal', 'weight', 'dial_color', 'numerals',
                   'short_description']

data = data.drop(columns_to_drop, axis=1)


# replace every row that ends with h into hours
data['power_reserve'] = data['power_reserve'].str.replace("h", "hours")
data['power_reserve'] = data['power_reserve'].str.replace("hoursours", "hours")

# remove <p> tag
data['description'] = data['description'].str.replace("<p>", "")
data['description'] = data['description'].str.replace("</p>", "")

# saving the dataframe into CSV file
data.to_csv('../data/Cleaned_data.csv', index=False)