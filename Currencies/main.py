import webscraping
import plik


plik.saving_euro()
plik.saving_dolar()

def analysis_euro():

    with open('euro.csv', 'r', encoding='utf-8') as reader:

        df = pd.read_csv(reader)
        df.columns = 'Data', 'Kurs'
        df['Data'] = pd.to_datetime(df['Data']).dt.date

        #tutaj trzeba jakąś analitykę

def analysis_dolar():
    pass



webscraping.compare()
webscraping.where_buy_euro()
webscraping.where_sell_euro()
webscraping.where_buy_dolar()
webscraping.where_sell_dolar()