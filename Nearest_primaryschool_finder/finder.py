import math
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

file = 'warsaw_primary_schools.xlsx'


def add_coordinates(df):
    url_beginning = r"https://www.google.pl/maps/place/"
    df['Latitude'] = '0'
    df['Longitude'] = '0'

    for index, row in df.itterrows():
        URL = url_beginning + row[16] + r"+" + str(row[17]) + r",+" + row[19] + "+Warszawa"
        page = get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        for object in soup.find_all('div', class_='mLuXec'):
            price = object.find('div', class_='mLuXec').get_text().strip().split(", ")
            df[index, 'Latitude'] = price[0]
            df[index, 'Longitude'] = price[1]

    return df


def finder(df: object, city: object, street: object, number: object, postalcode: object) -> object:
    url_beginning = r"https://www.google.pl/maps/place/"
    URL = url_beginning + street + r"+" + str(number) + r",+" + postalcode + "+" + city
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for object in soup.find_all('div', class_='mLuXec'):
        price = object.find('div', class_='mLuXec').get_text().strip().split(", ")
        lat_user = price[0]
        lon_user = price[1]

    df['distance'] = [sqrt(pow((price[0] - df['Latitude']), 2) + pow((price[1] - df['Longitude']), 2))]

    minim = min(df['distance'])
    return df[df['distance'] == minim]


def find_school(logop, psychologist, pedagogue, language, students, school_type):
    data = pd.read_excel(file)
    df = data.loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy', 'Strona www', data['Publiczność status'].isin(school_type),
                     data['Kategoria uczniów'].eq(students), data["Języki nauczane"].str.contains(language).any(), data["Czy zatrudnia logopedę"].isin(logop),
                     data["Czy zatrudnia pedagoga"].isin(pedagogue), data["Czy zatrudnia psychologa"].isin(psychologist)]]

    schools = add_coordinates(df)

    return finder(schools)