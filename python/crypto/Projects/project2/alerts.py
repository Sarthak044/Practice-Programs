import os
import csv
import sys
import json
import time
import requests
from datetime import datetime

#DECLARATION
local_currency = "INR"
local_symbol = "₹"
api_key = "b14a28cc-f644-4cf5-b38c-37b2852f9f41"
headers1 = {"X-CMC_PRO_API_KEY": api_key} # Default and same
base_url = "https://pro-api.coinmarketcap.com"

print("\nAlerts Tracking ...\n")

already_hit_symbols = []
try:
    while True:
        with open("/home/sk/Documents/codes/python/crypto/Projects/project2/alerts.csv","r") as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                if '\ufeff' in line[0]:
                    line[0] = line[0][1:].upper()
                else:
                    line[0] = line[0].upper()
                amount = line[1]
                symbol = line[0]

                quote_url = base_url + "/v1/cryptocurrency/quotes/latest?convert=" + local_currency + "&symbol=" + symbol
                request = requests.get(quote_url, headers=headers1)
                results = request.json()

                currency = results['data'][symbol]
                name = currency['name']
                price = currency['quote'][local_currency]['price']

                if float(price) >= float(amount) and symbol not in already_hit_symbols:
                    now = datetime.now()
                    current_time = now.strftime("%I:%M%p")
                    os.system('say ALERT ALERT ALERT ')
                    os.system("say  '{}hit{}at{}' ".format(name,amount,current_time))
                    sys.stdout.flush()
                    print(name + " hit " + amount + " at " + current_time)
                    already_hit_symbols.append(symbol)
        print("...")
        time.sleep(10)

except KeyboardInterrupt:
    print(" Captured CTRL^C")
    print("Exiting...")
    