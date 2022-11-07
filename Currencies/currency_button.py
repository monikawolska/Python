from kivy.properties import BooleanProperty
from kivy.uix.button import Button


class CurrencyButton(Button):
    selected = BooleanProperty(False)