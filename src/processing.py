#!/usr/bin/env python3
# you should chmod this file before using run.py --> chmod +x processing.py

import pandas as pd
import re

data = pd.read_csv('../data/Corum_timestamp.csv')

# Dropping the empty columns
columns_to_drop = ['type', 'year_introduced', 'style', 'case_shape',
                   'case_finish', 'caseback', 'lug_to_lug', 'bezel_material',
                   'bezel_color', 'crystal', 'weight', 'dial_color', 'numerals',
                   'short_description']

data = data.drop(columns_to_drop, axis=1)


# format price rows
data['price'] = data['price'].str.replace(' ', '')
data['price'] = data['price'].str.replace(',', '.')
data['price'] = data['price'].astype(float)

# Cnovert currency from CHF to USD
# Exchange rate from CHF to USD
exchange_rate_CHF_to_USD = 1.10  # For example, 1 CHF = 1.10 USD

# Function to convert currency from CHF to USD
def convert_currency(amount_CHF):
    return round(amount_CHF * exchange_rate_CHF_to_USD, 2)

data['price'] = data['price'].apply(convert_currency)
data['currency'] = data['currency'].str.replace("CHF", "USD")

# replace every row that ends with h into hours
data['power_reserve'] = data['power_reserve'].str.replace("h", "hours")
data['power_reserve'] = data['power_reserve'].str.replace("hoursours", "hours")

    
# remove HTML tags from description column
def remove_htmlTags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Apply fillna before cleaning process to handle empty rows
# Apply the function to the description column and remove the Square Brackets []
data['description'] = data['description'].fillna('').apply(remove_htmlTags).str.strip('[]')


# saving the dataframe into CSV file
data.to_csv('../data/Cleaned_data.csv', index=False)