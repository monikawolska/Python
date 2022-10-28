from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import analysis


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1000')
Config.set('graphics', 'fullscreen', '0')

euro = analysis.Analysis("euro.csv", "EURO", "https://www.money.pl/pieniadze/nbparch/srednie/?symbol=EUR.n", "EUR")
dolar = analysis.Analysis("dolar.csv", "DOLAR", "https://www.money.pl/pieniadze/nbparch/srednie/?symbol=USD", "USD")

#plt.plot(euro.x(200), euro.y(200))
#plt.show()

class Invest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #chart = self.ids.chart
        #plt.plot(euro.default_chart_x(), euro.default_chart_y())
        #chart.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    def show_data_euro(self):
        self.ids.current_price_date.text = euro.price_today_data()
        self.ids.current_price.text = euro.price_today()
        self.ids.currency_info.text = euro.rolling_average()

    def show_data_dolar(self):
        self.ids.current_price_date.text = dolar.price_today_data()
        self.ids.current_price.text = dolar.price_today()
        self.ids.currency_info.text = dolar.rolling_average()

    def update(self):
        euro.updating_currency()
        dolar.updating_currency()


    def show_chart_200(self):
        chart = self.ids.chart
        plt.plot(euro.x(200), euro.y(200))
        chart.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    def show_chart_50(self):
        chart = self.ids.chart
        plt.plot(euro.x(50), euro.y(50))
        chart.add_widget(FigureCanvasKivyAgg(plt.gcf()))


    def show_chart_7(self):
        chart = self.ids.chart
        plt.plot(euro.x(7), euro.y(7))
        chart.add_widget(FigureCanvasKivyAgg(plt.gcf()))


class InvestApp(App):

    def build(self):
        return Invest()


if __name__ == '__main__':
    InvestApp().run()
