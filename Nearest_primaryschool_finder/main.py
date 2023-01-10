from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '1500')
Config.set('graphics', 'fullscreen', '0')


class Finder(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def update(self):
        pass

    def logopedist_click(self):
        pass

    def switchstate1(self):
        pass

    def switchstate2(self):
        pass

class FinderApp(App):

    def build(self):
        return Finder()


if __name__ == '__main__':
    FinderApp().run()