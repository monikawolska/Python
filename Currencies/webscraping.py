import pprint
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

eur_buy = []
eur_sell = []
dol_buy = []
dol_sell = []
source = []


def comma_to_dot(word):
    liczba = ""
    for letter in word:
        if letter == ',':
            liczba = liczba + '.'
        else:
            liczba = liczba + letter

    return liczba


def current_prices():
    prices = pd.DataFrame(list(zip(eur_buy, eur_sell, dol_buy, dol_sell, source)))
    prices.columns = 'Euro: kurs kupna', 'Euro: kurs sprzedaży', 'Dolar: kurs kupna', 'Dolar: kurs sprzedaży', 'Strona'
    pd.to_numeric(prices['Euro: kurs kupna'])
    pd.to_numeric(prices['Euro: kurs sprzedaży'])
    pd.to_numeric(prices['Dolar: kurs kupna'])
    pd.to_numeric(prices['Dolar: kurs sprzedaży'])

    return prices


def where_buy_euro():
    price = min(eur_sell)
    website = source[(eur_sell.index(price))]
    print(price, website)


def where_buy_dolar():
    price = min(dol_sell)
    website = source[(dol_sell.index(price))]
    print(price, website)


def where_sell_euro():
    price = max(eur_buy)
    website = source[(eur_buy.index(price))]
    print(price, website)


def where_sell_dolar():
    price = max(dol_buy)
    website = source[(dol_buy.index(price))]
    print(price, website)


def internetowyKantor():
    URL = 'https://internetowykantor.pl/kursy-walut/'
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    k = 1
    for object in soup.find_all(class_="bem-rate-table__rate"):
        price = object.find().get_text().strip()

        if k == 1:
            eur_buy.append(comma_to_dot(price))
            source.append(URL)
        elif k == 2:
            eur_sell.append(comma_to_dot(price))
        elif k == 4:
            dol_buy.append(comma_to_dot(price))
        elif k == 5:
            dol_sell.append(comma_to_dot(price))
            break
        k += 1


def walutomat():
    URL = 'https://www.walutomat.pl/kursy-walut/'
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for object in soup.find_all('tr', class_='EUR_PLN'):
        price = object.find('span', class_='buy').get_text().strip()
        eur_buy.append(comma_to_dot(price))
        price = object.find('span', class_='sell').get_text().strip()
        eur_sell.append(comma_to_dot(price))
    for object in soup.find_all('tr', class_='USD_PLN'):
        price = object.find('span', class_='buy').get_text().strip()
        dol_buy.append(comma_to_dot(price))
        price = object.find('span', class_='sell').get_text().strip()
        dol_sell.append(comma_to_dot(price))

    source.append(URL)


def liderWalut():

    URL = 'https://liderwalut.pl/kursy-walut/kurs-dolara'
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for object in soup.find_all('tr', class_="EUR"):
        price = object.find('td', class_='bid stay').get_text().strip()
        eur_buy.append(price)
        price = object.find('td', class_='ask stay').get_text().strip()
        eur_sell.append(price)
    for object in soup.find_all('tr', class_="USD"):
        price = object.find('td', class_='bid stay').get_text().strip()
        dol_buy.append(price)
        price = object.find('td', class_='ask stay').get_text().strip()
        dol_sell.append(price)

    source.append(URL)


def compare():
    internetowyKantor()
    walutomat()
    liderWalut()

