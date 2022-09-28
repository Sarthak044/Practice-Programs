#!/usr/bin/python3

#PORTFOLIO PROJECT

#IMPORTS
from colorama import Fore, Back, Style
from prettytable import PrettyTable as pt
import json
import requests
import os
import csv


#DECLARATION
local_currency = 'INR'
local_symbol = '₹'
api_key = 'b14a28cc-f644-4cf5-b38c-37b2852f9f41'
headers1 = {'X-CMC_PRO_API_KEY': api_key} # Default and same
base_url = 'https://pro-api.coinmarketcap.com'

# HEADER
print()
print("\t\t\tMY PORTFOLIO")
print()

# TABLE
portfolio_value = 0.0

table = pt(['Assest', 'Amount Owned', 'Value', 'Price', '1H', '24H', '7D'])

with open("/home/sk/Documents/codes/python/crypto/Projects/project1/myportfolio.csv", "r") as csv_file:
    csv_r = csv.reader(csv_file)
    for line in csv_r:
        if '\ufeff' in line[0]:
            line[0] = line[0][1:].upper()
        else:
            line[0] = line[0].upper()
        
        symbol = line[0]
        amount = line[1]
        
        quote_url = base_url + '/v1/cryptocurrency/quotes/latest?convert=' + local_currency + "&symbol=" + symbol
        request = requests.get(quote_url, headers=headers1)
        results = request.json()
        
        #print(json.dumps(results, sort_keys=True, indent=4))
        
        currency = results['data'][symbol]
        name = currency['name']
        quote = currency['quote'][local_currency]
        
        hour_change = round(quote['percent_change_1h'],1)
        day_change = round(quote['percent_change_24h'],1)
        week_change = round(quote['percent_change_7d'],1)
        
        price = quote['price']

        value = float (price) * float(amount)
        portfolio_value += value
        
        price_string = '{:,}'.format(round(price,2)) 
        value_string = '{:,}'.format(round(value,2))

        table.add_row([name +' (' + symbol + ')',
                       amount,
                       local_symbol+value_string,
                       local_symbol+price_string,
                       str(hour_change),
                       str(day_change),
                       str(week_change)])

print(table)
