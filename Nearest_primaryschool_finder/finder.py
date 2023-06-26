import math
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

file = 'warsaw_primary_schools.xlsx'


def add_coordinates(df):
    url_beginning = r"https://www.google.pl/maps/place/"
    df['Latitude'] = 0
    df['Longitude'] = 0

    for index, row in df.iterrows():
        URL = url_beginning + row[1] + r"+" + str(row[2]) + r",+" + row[4] + "+Warszawa"
        page = get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')

        for object in soup.find_all('div', class_='mLuXec'):
            price = object.find('div', class_='mLuXec').get_text().strip().split(", ")
            df[index, 'Latitude'] = price[0]
            df[index, 'Longitude'] = price[1]

    return df

def finder(df, city, street, number, postalcode):
    url_beginning = r"https://www.google.pl/maps/place/"
    URL = url_beginning + street + r"+" + str(number) + r",+" + postalcode + "+" + city
    page = get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')

    for object in soup.find_all('div', class_='mLuXec'):
        price = object.find('div', class_='mLuXec').get_text().strip().split(", ")
        lat_user = float(price[0])
        lon_user = float(price[1])

    df['distance'] = [math.sqrt(pow((lat_user - df['Latitude']), 2) + pow((lon_user - df['Longitude']), 2))]

    minim = min(df['distance'])
    return df[df['distance'] == minim][0]


def find_school(logop, psychologist, pedagogue, language, students, school_type):
    data = pd.read_excel(file)
    df = data[data['Publiczność status'].isin(school_type) &
                      data['Kategoria uczniów'].isin(students) &
                      data["Języki nauczane"].str.contains(language).any() &
                      data["Czy zatrudnia logopedę"].isin(logop) &
                      data["Czy zatrudnia pedagoga"].isin(pedagogue) &
                      data["Czy zatrudnia psychologa"].isin(psychologist)].loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy']]

    schools = add_coordinates(df)

    return schools
