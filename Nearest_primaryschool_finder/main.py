from kivy.app import App
from kivy.config import Config
from kivy.uix.pagelayout import PageLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import finder

Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '1500')
Config.set('graphics', 'fullscreen', '0')


class Finder(PageLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    information_students_type = []
    information_school_type = []
    information_logop_click = []
    information_psychologist_click = []
    information_pedagogue_click = []
    information_language_click = ''

    def students_type(self, instance, value, answer):
        if value:
            self.information_students_type = answer
            return tuple(self.information_students_type)

    def school_type(self, instance, value, answer):
        if value:
            self.information_school_type = answer
            return tuple(self.information_school_type)

    def logop_click(self, instance, value, answer):
        if value:
            self.information_logop_click = answer
            return tuple(self.information_logop_click)

    def psychologist_click(self, instance, value, answer):
        if value:
            self.information_psychologist_click = answer
            return tuple(self.information_psychologist_click)

    def pedagogue_click(self, instance, value, answer):
        if value:
            self.information_pedagogue_click = answer
            return tuple(self.information_pedagogue_click)

    def language_click(self, instance, value, answer):
        if value:
            self.information_language_click = answer
            return str(self.information_language_click)

    def nearest_school(self):

        df = finder.find_school(self.information_logop_click, self.information_psychologist_click,
                                self.information_pedagogue_click,
                                self.information_language_click, self.information_students_type,
                                self.information_school_type)
        self.ids.result.text = finder.finder(df, self.ids.address_city.text, self.ids.address_street.text,
                                             self.ids.address_house.text, self.ids.address_code.text)


class FinderApp(App):

    def build(self):
        return Finder()


if __name__ == '__main__':
    FinderApp().run()
