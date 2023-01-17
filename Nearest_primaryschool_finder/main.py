from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import finder

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '1500')
Config.set('graphics', 'fullscreen', '0')


class Finder(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def students_type(self, instance, value, answer):
        if value == True:
            return answer
    def school_type(self, instance, value, answer):
        if value == True:
            return answer
    def logopedist_click(self, instance, value, answer):
        if value == True:
            return answer
    def psychologist_click(self, instance, value, answer):
        if value == True:
            return answer
    def pedagogue_click(self, instance, value, answer):
        if value == True:
            return answer
    def language_click(self, instance, avalue, answer):
        if value == True:
            return answer

    def answer(self, id):
        return self.ids.text

    def nearest_school(self):

        df = finder.find_school(self.logopedist_click(), self.psychologist_click(), self.pedagogue_click(),
                           self.language_click(), self.students_type(), self.school_type())
        self.ids.result.text = finder.finder(df, self.answer(self, address_city), street, number, postalcode)

class FinderApp(App):

    def build(self):
        return Finder()

if __name__ == '__main__':
    FinderApp().run()
