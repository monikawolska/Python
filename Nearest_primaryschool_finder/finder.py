import math
import pandas as pd


file = 'warsaw_primary_schools.xlsx'
def schools():
    data = pd.read_excel(file)
    df = data.loc[:,['Nazwa', 'Ulica', 'Numer budynku', 'Numer lokalu', 'Kod pocztowy', 'Strona www', 'Publiczność status',
                     'Kategoria uczniów', 'Języki nauczane', 'Czy zatrudnia logopedę', 'Czy zatrudnia psychologa',
                     'Czy zatrudnia pedagoga']]
    return df


schools()

def user_data():
    #lokalizacja
    #Czy zatrudnia logopedę - tak, nie, wszystko
    #Czy zatrudnia psychologa - tak, nie, wszystko
    #Czy zatrudnia pedagoga - tak, nie, wszystko
    #Języki nauczane - angielski, niemiecki, hiszpański, rosyjski, francuski, arabski
    #najlepiej to żeby samo sprawdzało te języki
    pass


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

    # Driver code
    if __name__ == "__main__":
        lat1 = 51.5007
        lon1 = 0.1246
        lat2 = 40.6892
        lon2 = 74.0445

        print(haversine(lat1, lon1, lat2, lon2))
    pass