#!/usr/bin/python3

import requests
import json

# Variables/Setup/ENV
local_currency = 'INR'
local_symbol = '₹'
api_key = 'b14a28cc-f644-4cf5-b38c-37b2852f9f41'
headers1 = {'X-CMC_PRO_API_KEY': api_key}
base_url = 'https://pro-api.coinmarketcap.com'
global_url = base_url + '/v1/global-metrics/quotes/latest?convert=' + local_currency

# Requesting api for the crypto data
request = requests.get(global_url, headers=headers1)
results = request.json()

# Test print whole json api response
print(json.dumps(results,sort_keys=True, indent=4))

# Fetching individual data
# data = results["data"]
# btc_dominance = data["btc_dominance"]
# eth_dominance = data["eth_dominance"]
# total_marketcap = data["quote"][local_currency]["total_market_cap"]
# total_vol = data["quote"][local_currency]["total_volume_24h"]

# # Rounding off for clean view
# total_marketcap = round(total_marketcap, 2)
# btc_dominance = round(btc_dominance, 2)
# eth_dominance = round(eth_dominance, 2)
# total_vol = round(total_vol, 2)

# total_marketcap_string = local_symbol + '{:,}'.format(total_marketcap)
# total_vol_string = local_symbol + '{:,}'.format(total_vol)