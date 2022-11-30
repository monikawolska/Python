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

def finder():
    pass