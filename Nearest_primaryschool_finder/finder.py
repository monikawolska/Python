import math
import pandas as pd


file = 'warsaw_primary_schools.xlsx'


def finder(lat1, lon1, lat2, lon2):
# using harvestine formula
        dLat = (lat2 - lat1) * math.pi / 180.0
        dLon = (lon2 - lon1) * math.pi / 180.0

# converting to radians
        lat1 = (lat1) * math.pi / 180.0
        lat2 = (lat2) * math.pi / 180.0

# applying formula
        a = (pow(math.sin(dLat / 2), 2) +
             pow(math.sin(dLon / 2), 2) *
             math.cos(lat1) * math.cos(lat2));
        rad = 6371
        c = 2 * math.asin(math.sqrt(a))

        return rad * c


def find_school(logopedist, psychologist, pedagogue, language, students, school_type):
    data = pd.read_excel()
    df = data.loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy', 'Strona www', data['Publiczność status'].isin(school_type),
                     data['Kategoria uczniów'].eq(students), data["Języki nauczane"].str.constains(language), data["Czy zatrudnia logopedę"].isin(logopedist),
                     data["Czy zatrudnia pedagoga"].isin(pedagogue), data["Czy zatrudnia psychologa"].isin(psychologist)]]

    school = "Pass"
    return school





