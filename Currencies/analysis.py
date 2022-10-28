import pandas as pd
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import webscraping
import datetime
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import requests



class Analysis():

    def __init__(self, file=None, currency=None, url=None, code_iso=None):
        self.file = file
        self.currency = currency
        self.url = url
        self.data_frame = self._downloading_data()
        self.code_iso = code_iso

    def updating_currency(self):
        '''Pobieranie kursów waluty wg NBP'''

        today = datetime.date.today()
        oneday = datetime.timedelta(days=1)
        yesterday = today - oneday

        page = get(self.url, timeout=5)
        soup = BeautifulSoup(page.content, 'html.parser')

        with open(self.file, 'a', encoding='utf-8') as writer, open(self.file, 'r', encoding='utf-8') as reader:

            data_frame = pd.read_csv(reader)
            data_frame.columns = 'Data', 'Kurs'
            data_frame['Data'] = pd.to_datetime(data_frame['Data']).dt.date
            last_date = data_frame.iloc[-1, 0]

            while last_date < yesterday:

                last_date = last_date + oneday

                all = soup.find_all('div', class_="rt-td")
                for object in all:
                    pom = object.find().get_text()
                    try:
                        data = datetime.datetime.strptime(pom, "%Y-%m-%d")
                        data = data.date()
                        if data == last_date:
                            index = all.index(object) + 1
                            value = all[index]
                            value = value.find().get_text()
                            value = value[0] + "." + value[2:]
                            writer.writelines("\n" + str(data) + "," + value)
                            break
                    except ValueError:
                        continue


    def _downloading_data(self):

        with open(self.file, 'r', encoding='utf-8') as reader:
            data_frame = pd.read_csv(reader)
            data_frame.columns = 'Data', 'Kurs'
            data_frame['Data'] = pd.to_datetime(data_frame['Data']).dt.date
            data_frame['Kurs'] = pd.to_numeric(data_frame['Kurs'])

            data_frame['SMA200'] = data_frame['Kurs'].rolling(window=200).mean()
            data_frame['EMA200'] = data_frame['Kurs'].ewm(span=200).mean()

            data_frame['SMA60'] = data_frame['Kurs'].rolling(window=60).mean()
            data_frame['EMA60'] = data_frame['Kurs'].ewm(span=60).mean()

            data_frame['SMA7'] = data_frame['Kurs'].rolling(window=7).mean()
            data_frame['EMA7'] = data_frame['Kurs'].ewm(span=7).mean()

            return data_frame


    def price_today(self):
        response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/" +  self.code_iso +"/")
        fox = response.json()

        for key in fox['rates']:
            price = key['mid']

        return str(price)

    def price_today_data(self):
        response = requests.get("http://api.nbp.pl/api/exchangerates/rates/a/" +  self.code_iso +"/")
        fox = response.json()

        for key in fox['rates']:
            data = key['effectiveDate']

        return str(data)


    def rolling_average(self):
        # SMA - średia krocząca, EMA - wykładnicza średnia krocząca
        # EMA daje sygnał, SMA określa trend

        result = "Wg analizy średnich SMA200 i SMA7: "

        if (self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 6]).all() & (
                self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 4]).all():
            result = result + "Silny trend rosnący\n"
        elif (self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 6]).all():
            result = result + "Trend rosnący\n"
        elif (self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 6]).all() & (
                self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 4]).all():
            result = result + "Silny trend malejący\n"
        elif (self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 6]).all():
            result = result + "Trend malejący\n"
        else:
            result = result + "Brak długiego potwierdzonego trendu\n"

        #formacja złotego krzyża i formacja krzyża śmierci

        title = "Wg analizy średnich EMA200 i EMA7: "
        text = "EMA sygnalizuje dobry czas transakcji: "
        flag = 0

        for n in [-8,-7,-6,-5,-4,-3,-2,-1]:
            data = self.data_frame.iat[(n+1), 0]
            if (self.data_frame.iat[n, 7] < self.data_frame.iat[n, 3]) & (
                    self.data_frame.iat[(n+1), 7] > self.data_frame.iat[(n+1), 3]):
                flag = 1
                result = result + title + text + "kup\n" + "Data wystąpienia: " + data

                webscraping.compare()
                webscraping.where_buy(self.currency)
            elif (self.data_frame.iat[n, 7] > self.data_frame.iat[n, 3]) & (
                    self.data_frame.iat[(n+1), 7] < self.data_frame.iat[(n+1), 3]):
                flag = 1
                result = result + title + text + "sprzedaj\n" + "Data wystąpienia: " + data
                webscraping.compare()
                webscraping.where_sell(self.currency)

        if flag == 0:
                result = result + title + "Brak sygnału do kupna/sprzedaży\n"

        return result

    def default_chart_x(self):
        x = self.data_frame['Data']
        return x


    def default_chart_y(self):
        y = self.data_frame[['Kurs', 'SMA200', 'SMA7']]
        return y


    def x(self, number):
        n = (-number)
        x = self.data_frame.iloc[n:,0]
        y = self.data_frame.iloc[n:,[1,3,7]]
        return x


    def y(self, number):
        n = (-1)*number
        y = self.data_frame.iloc[n:,[1,3,7]]
        return y


    def ichimoku_strategy(self):
        pass


    def harmonic_Fibonacci_analysis(self):
        pass


    def simple_steps(self):

        number = -1

        if self.data_frame.iat[(number-1), 1] - self.data_frame.iat[(number-2), 1] < 0:
            text = "Cena spada od"
            while (self.data_frame.iat[(number-1), 1] - self.data_frame.iat[(number-2), 1] < 0) & (
                    abs(number) <= 20):
                number =- 1
        elif self.data_frame.iat[(number-1), 1] - self.data_frame.iat[(number-2), 1] > 0:
            while self.data_frame.iat[(number-1), 1] - self.data_frame.iat[(number-2), 1] > 0 & (
                    abs(number) >= 20):
                number =- 1
            text = "Cena rośnie od "

        print(text + abs(number))

euro = Analysis("euro.csv", "EURO", "https://www.money.pl/pieniadze/nbparch/srednie/?symbol=EUR.n", "EUR")
