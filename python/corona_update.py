import sys
import pyfiglet
from pyfiglet import Figlet
try:
    import requests
except ImportError:
    print("Please Install Requests Module With Command 'pip install requests'")
    sys.exit(1)
from time import sleep

url = "https://api.covid19api.com/summary"
visit = requests.get(url).json()

NewConfirmed = visit['Global']['NewConfirmed']
TotalConfirmed = visit['Global']['TotalConfirmed']
NewDeaths = visit['Global']['NewDeaths']
TotalDeaths = visit['Global']['TotalDeaths']
NewRecovered = visit['Global']['NewRecovered']
TotalRecovered = visit['Global']['TotalRecovered']

india = visit['Countries']
name = india[76]['Country']
indiaconfirmed = india[76]['NewConfirmed']
indiatotal = india[76]['TotalConfirmed']
indiaDeaths = india[76]['NewDeaths']
deathstotal = india[76]['TotalDeaths']
indianewr = india[76]['NewRecovered']
totalre = india[76]['TotalRecovered']
DateUpdate = india[76]['Date']


def world():
    fig = Figlet(font='doom')
    print(fig.renderText(f"TOTAL CASES IN THE WORLD"))
    print ('''New Confirmed Cases :- {NewConfirmed}
    Total Confirmed Cases :- {TotalConfirmed}
    New Deaths :- {NewDeaths}
    Total Deaths :- {TotalDeaths}
    New Recovered :- {NewRecovered}
    Total Recovered :- {TotalRecovered}
    ''')

def indiac():
    fig = Figlet(font='doom')
    print(fig.renderText(f"INDIA"))
    print('''
Country Name :- {name}
New Confirmed Cases :- {indiaconfirmed}
Total Confirmed Cases :- {indiatotal}
New Deaths :- {indiaDeaths}
Total Deaths :- {deathstotal}
New Recovered :- {indianewr}
Total Recovered :- {totalre}
Information Till :- {DateUpdate}''')

    


fig = pyfiglet.figlet_format("CORONA VIRUS", font='slant')
print(fig)
print("\nDeveloped By @saurabh sharma")


def choices():
    print("\n1 - To Know Corona Virus Update Across World")
    print("\n2 - To Know Corona Virus Update In India")
    choice = input("Enter 1 Or 2 :- ")

    if choice == "1":
        world()
        sleep(1)
        choices()
    
    elif choice == "2":
        indiac()
        sleep(1)
        choices()
    
    else:
        print("\nYou Have Entered Something Wrong, Please Enter Again")
        choices()
    


choices()
