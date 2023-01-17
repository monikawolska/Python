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
            df[index, 'Latitude'] = price[1]

    return df


def finder(df):


    lat1, lon1, lat2, lon2
    # using harvestine formula
    dLat = (lat2 - lat1) * math.pi / 180.0
    dLon = (lon2 - lon1) * math.pi / 180.0

    # converting to radians
    lat1 = (lat1) * math.pi / 180.0
    lat2 = (lat2) * math.pi / 180.0

    # applying formula
    a = (pow(math.sin(dLat / 2), 2) +
         pow(math.sin(dLon / 2), 2) *
         math.cos(lat1) * math.cos(lat2))

    rad = 6371
    c = 2 * math.asin(math.sqrt(a))

    return rad * c


def find_school(logopedist, psychologist, pedagogue, language, students, school_type):
    data = pd.read_excel()
    df = data.loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy', 'Strona www', data['Publiczność status'].isin(school_type),
                     data['Kategoria uczniów'].eq(students), data["Języki nauczane"].str.constains(language), data["Czy zatrudnia logopedę"].isin(logopedist),
                     data["Czy zatrudnia pedagoga"].isin(pedagogue), data["Czy zatrudnia psychologa"].isin(psychologist)]]

    schools = add_coordinates(df)

    return finder(schools)


