import datetime
from requests import get
from bs4 import BeautifulSoup
import pandas as pd



def saving_euro():

    plik = 'euro.csv'

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday

    URL = 'https://www.money.pl/pieniadze/nbparch/srednie/?symbol=EUR.n'
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    with open(plik, 'a', encoding='utf-8') as writer, open(plik, 'r', encoding='utf-8') as reader:

        df = pd.read_csv(reader)
        df.columns = 'Data', 'Kurs'
        df['Data'] = pd.to_datetime(df['Data']).dt.date
        last_date = df.iloc[-1,0]

        while last_date < today:

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


def saving_dolar():
    plik = 'dolar.csv'

    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday

    URL = 'https://www.money.pl/pieniadze/nbparch/srednie/?symbol=USD'
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    with open(plik, 'a', encoding='utf-8') as writer, open(plik, 'r', encoding='utf-8') as reader:

        df = pd.read_csv(reader)
        df.columns = 'Data', 'Kurs'
        df['Data'] = pd.to_datetime(df['Data']).dt.date
        last_date = df.iloc[-1, 0]

        while last_date < today:

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




