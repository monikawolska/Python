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


def finder(df, city, street, number, postalcode):

    URL = url_beginning + street + r"+" + str(number) + r",+" + postalcode + "+" + city
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for object in soup.find_all('div', class_='mLuXec'):
        price = object.find('div', class_='mLuXec').get_text().strip().split(", ")
        lat_user = price[0]
        lon_user = price[1]

    for index, row in df.itterrows():

        lat = df[index, 'Latitude']
        lon = df[index, 'Longitude']

        # using harvestine formula
        dLat = (lat_user - lat) * math.pi / 180.0
        dLon = (lon_user - lon) * math.pi / 180.0

        # converting to radians
        lat = (lat) * math.pi / 180.0
        lat_user = (lat_user) * math.pi / 180.0

        # applying formula
        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
             math.cos(lat) * math.cos(lat_user))

        rad = 6371
        c = 2 * math.asin(math.sqrt(a))
        distance = rad * c

        if index == 0:
            min = distance
            indeks_result = 0
        else:
            if distance < min:
                min = distance
                indeks_result = index

    return df[indeks_result, :]


def find_school(logopedist, psychologist, pedagogue, language, students, school_type):
    data = pd.read_excel()
    df = data.loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy', 'Strona www', data['Publiczność status'].isin(school_type),
                     data['Kategoria uczniów'].eq(students), data["Języki nauczane"].str.constains(language), data["Czy zatrudnia logopedę"].isin(logopedist),
                     data["Czy zatrudnia pedagoga"].isin(pedagogue), data["Czy zatrudnia psychologa"].isin(psychologist)]]

    schools = add_coordinates(df)

    return finder(schools)


