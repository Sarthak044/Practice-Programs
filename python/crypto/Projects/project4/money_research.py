#!/usr/bin/python3

import json
import math
import requests
from prettytable import PrettyTable
import locale

#DECLARATION
# locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
local_currency = 'INR'
local_symbol = '₹'
api_key = 'b14a28cc-f644-4cf5-b38c-37b2852f9f41'
headers1 = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

request = requests.get(global_url, headers=headers1)
results = request.json()

# print(json.dumps(results,sort_keys=True, indent=4))

data = results["data"]

total_marketcap = data["quote"][local_currency]["total_market_cap"]
total_marketcap_string = '{:,}'.format(total_marketcap)

table = PrettyTable(['Name', 'Ticker', 'percent of total global cap', 'Current', 'Gold(10.9T)', 'Narrow Money(35.2T)', 'Stock Market(89.5T)'])

listing_url = base_url + '/v1/cryptocurrency/listings/latest?convert='+local_currency

request = requests.get(listing_url, headers=headers1)
results = request.json()

data = results['data']

for currency in data:
    name = currency['name']
    ticker = currency['symbol']
    market_cap = currency['quote'][local_currency]['market_cap']
    percentage_of_global_cap = float(market_cap) / float(total_marketcap)
    price = currency['quote'][local_currency]['price']
    available_supply = currency['total_supply']
    gold_price = 10900000000000 * percentage_of_global_cap / available_supply
    narrow_price = 35200000000000 * percentage_of_global_cap / available_supply
    stock_price = 89500000000000 * percentage_of_global_cap / available_supply
    
    percentage_of_global_cap_string = str(round(percentage_of_global_cap*100,2)) + '%'
    price_string = local_symbol + str(price)
    gold_price_string = local_symbol + '{:,}'.format(round(gold_price,2))
    narrow_price_string = local_symbol + '{:,}'.format(round(narrow_price,2))
    stock_price_string = local_symbol + '{:,}'.format(round(stock_price,2))

    table.add_row([name,ticker,percentage_of_global_cap_string,price_string,gold_price_string,narrow_price_string,stock_price_string])


print()
print(table)
print()