
# READ INVENTORY OF PRODUCTS

#products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
#products_df = read_csv(products_filepath)
#products = products_df.to_dict("records")

import os
import pandas as pd
from app.utils import to_usd
products_csv_filepath = os.path.isfile(os.path.join(os.path.dirname(__file__), "..", "data", "products.csv"))
default_products_csv = os.path.join(os.path.dirname(__file__), "..", "data", "default_products.csv")





# checks to see if a products.csv file exists. If not, it uses the default
if products_csv_filepath == True:
    print("USING CUSTOM PRODUCTS CSV FILE...")
    csv_filepath = products_csv_filepath
else:
    print("USING DEFAULT PRODUCTS CSV FILE...")
    csv_filepath = default_products_csv


from pandas import read_csv

#reads the csv file into products variable
products = read_csv(csv_filepath)
#pandas transforms the data into a list of dictionaries
products = products.to_dict('records')



# PRINTED INVENTORY REPORT

print("---------")
print("THERE ARE", len(products), "PRODUCTS:")
print("---------")

all_prices = []
for p in products:
    print("..." + p["name"] + "   " + to_usd(p["price"]))
    all_prices.append(float(p["price"]))

import statistics
avg_price = statistics.median(all_prices)

print("---------")
print("AVERAGE PRICE:", to_usd(avg_price))






# EMAIL INVENTORY REPORT
