from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.anchorlayout import  AnchorLayout


from kivymd.app import  MDApp
from kivymd.uix.chip import  MDChip

from kivy.core.window import  Window

Window.softinput_mode = "below_target"



class LogIn(AnchorLayout):
    pass

class ValleGestionApp(MDApp):
    
    def __init__(self, **kwargs):
        self.title = "Valle Gestion"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightBlue"
        super().__init__(**kwargs)

    def build(self):
       self.root = Builder.load_file("./libs/kv/log_in.kv")
        

   

if __name__ == "__main__":
    ValleGestionApp().run()