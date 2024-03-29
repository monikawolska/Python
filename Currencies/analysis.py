from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import argrelextrema
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


    def rolling_average_trends(self):
        # SMA - średia krocząca, EMA - wykładnicza średnia krocząca
        # EMA daje sygnał, SMA określa trend

        if (self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 6]).all() & (
                self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 4]).all():
            result = "Silny trend rosnący\n"
        elif (self.data_frame.iloc[-7:, 2] < self.data_frame.iloc[-7:, 6]).all():
            result = "Trend rosnący\n"
        elif (self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 6]).all() & (
                self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 4]).all():
            result = "Silny trend malejący\n"
        elif (self.data_frame.iloc[-7:, 2] > self.data_frame.iloc[-7:, 6]).all():
            result = "Trend malejący\n"
        else:
            result = "Brak długiego potwierdzonego trendu\n"

        return result


    def show_chart(self, number):
        df = self.data_frame[number:]
        x = df[['Data']]
        y = df[['Kurs', 'SMA200', 'SMA7']]
        plt.plot(x, y)
        return plt


    def rolling_average_signals(self):
        # formacja złotego krzyża i formacja krzyża śmierci
        flag = 0
        for n in [-8,-7,-6,-5,-4,-3,-2,-1]:
            data = self.data_frame.iat[(n+1), 0]
            if (self.data_frame.iat[n, 7] < self.data_frame.iat[n, 3]) & (
                    self.data_frame.iat[(n+1), 7] > self.data_frame.iat[(n+1), 3]):
                flag = 1
                result = "Sygnał kupna\n" + "Data wystąpienia: " + data

                webscraping.compare()
                webscraping.where_buy(self.currency)
            elif (self.data_frame.iat[n, 7] > self.data_frame.iat[n, 3]) & (
                    self.data_frame.iat[(n+1), 7] < self.data_frame.iat[(n+1), 3]):
                flag = 1
                result = "Sygnał sprzedaży\n" + "Data wystąpienia: " + data
                webscraping.compare()
                webscraping.where_sell(self.currency)

        if flag == 0:
                result = "Brak sygnału do kupna/sprzedaży\n"

        return result


    def ichimoku_strategy(self):
        pass


    def harmonic_Fibonacci_analysis(self):
        #finding relative extrema
        df = self.data_frame.iloc[-100:0]
        df_kurs = df['Kurs']

        for i in range(100, len(df)):

            max_idx = list(argrelextrema(df_kurs[:i], np.greater,order = 10)[0])
            min_idx = list(argrelextrema(df_kurs[:i], np.less, order = 10)[0])

            idx = max_idx + min_idx + [len(price_kurs[:i])-1]
            idx.sort()

            current_idx = idx[-5:]

            current_pat = df_kurs[current_idx]

            XA = current_pat[1] - current_pat[0]
            AB = current_pat[2] - current_pat[1]
            BC = current_pat[3] - current_pat[2]
            CD = current_pat[4] - current_pat[3]

            if XA>0 and AB<0 and BC>0 and CD<0:
                plt.plot(np.arange(start, i), df_kurs[start:i])
            plt.plot(current_idx, current_pat,c='r')
            plt.show()

            return string(max_idx)


    def simple_steps(self):
        pass