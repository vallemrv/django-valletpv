from kivy.app import App
from kivy.uix.label import  Label

class AppComandas(App):
    def build(self):
        return Label(text="holalalalala")

if __name__ == "__main__":
    AppComandas().run()