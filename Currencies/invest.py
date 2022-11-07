from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
import analysis
import currency_button


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '1000')
Config.set('graphics', 'fullscreen', '0')


euro = analysis.Analysis("euro.csv", "EURO", "https://www.money.pl/pieniadze/nbparch/srednie/?symbol=EUR.n", "EUR")
dolar = analysis.Analysis("dolar.csv", "DOLAR", "https://www.money.pl/pieniadze/nbparch/srednie/?symbol=USD", "USD")


class Invest(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #chart = self.ids.chart
        #plt.plot(euro.default_chart_x(), euro.default_chart_y())
        #chart.add_widget(FigureCanvasKivyAgg(plt.gcf()))

    def show_data_euro(self):
        self.deactivate_button()
        self.ids.euro_button.selected = not self.ids.euro_button.selected
        self.ids.current_price_date.text = euro.price_today_data()
        self.ids.current_price.text = euro.price_today()
        self.ids.trend_info.text = euro.rolling_average_trends()
        self.ids.transaction_info.text = euro.rolling_average_signals()

    def show_data_dolar(self):
        self.deactivate_button()
        self.ids.dolar_button.selected = not self.ids.dolar_button.selected
        self.ids.current_price_date.text = dolar.price_today_data()
        self.ids.current_price.text = dolar.price_today()
        self.ids.trend_info.text = dolar.rolling_average_trends()
        self.ids.transaction_info.text = dolar.rolling_average_signals()

    def update(self):
        euro.updating_currency()
        dolar.updating_currency()

    def show_chart_200(self):
        if (self.ids.euro_button.selected):
            result = euro.show_chart_200()
            self.ids.chart.add_widget(FigureCanvasKivyAgg(result.gcf()))
        elif (self.ids.dolar_button.selected):
            result = dolar.show_chart_200()
            self.ids.chart.add_widget(FigureCanvasKivyAgg(result.gcf()))

    def deactivate_button(self):
        self.ids.euro_button.selected = False
        self.ids.dolar_button.selected = False

class InvestApp(App):

    def build(self):
        return Invest()


if __name__ == '__main__':
    InvestApp().run()
