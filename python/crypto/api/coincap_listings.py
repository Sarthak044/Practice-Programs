#!/usr/bin/python3

import requests
import json

# Variables/Setup/ENV
local_currency = 'INR'
local_symbol = '₹'
api_key = 'b14a28cc-f644-4cf5-b38c-37b2852f9f41'
headers1 = {'X-CMC_PRO_API_KEY': api_key} # Default and same
base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/cryptocurrency/listings/latest?convert=' + local_currency

# Requesting api for the crypto data
request = requests.get(global_url, headers=headers1)
results = request.json()

# Test print whole json api response
# print(json.dumps(results,sort_keys=True, indent=4))

# Fetching individual data
data = results["data"]

for currency in data:
    name = currency['name']
    symbol = currency['symbol']

    #Fetching individual values from list of data
    price = currency['quote'][local_currency]['price']
    percent_ch = currency['quote'][local_currency]['percent_change_24h']
    market_cap = currency['quote'][local_currency]['market_cap']
    
    # Rounding OFF
    price = round(price,2)
    percent_ch = round(percent_ch,2)
    market_cap = round(market_cap,2)

    #Adding appropriate commas in the values
    price_str = local_symbol + '{:,}'.format(price)
    percent_ch_str = local_symbol + '{:,}'.format(percent_ch)
    market_cap_str = local_symbol + '{:,}'.format(market_cap)

    #Printing Stuff
    print('{}({})'.format(name,symbol))
    print('Price: {}'.format(price_str))
    print('24H Changes: {}'.format(percent_ch_str))
    print('Market Cap: {}'.format(market_cap_str))