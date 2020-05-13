import os
import json
import urllib
from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.screenmanager import  ScreenManager
from kivy.network.urlrequest import UrlRequest
from kivy.properties import BooleanProperty, ListProperty, ObjectProperty
from kivy.clock import  Clock
from kivy import  platform

from kivymd.app import MDApp

from oscpy.client import OSCClient
from oscpy.server import OSCThreadServer


from libs import SingUp, SingIn, AppMain

SPINNER = '''
Screen:
    name: 'spinner'
    MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True

    MDLabel:
        size_hint: .5, .5
        pos_hint: {'center_x': .6, 'center_y': .4}
        text: app.men_info_loading
'''

class ValleTPVAPP(MDApp):
   
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = "Find server"
        self.theme_cls.theme_sytle = "Light"
        self.theme_cls.prymary_palette = "LightBlue"
        self.title = "Valle TPV"
        App.navigation = []
        App.men_info_loading = "Haciendo comprobaciones ..."
    
    
    def build(self):
        App.sm = ScreenManager()
        App.sm.add_widget(AppMain())
        App.sm.add_widget(SingIn())
        App.sm.add_widget(SingUp())
        App.sm.add_widget(Builder.load_string(SPINNER))
        App.sm.current = "spinner"
        self.root = App.sm
        Clock.schedule_once(self.loadding, 0.5)

    def loadding(self, dt=0):
        if "credentials" in App.tpv_config:
            self.try_logging()
        else:
            App.sm.transition.direction = 'left'
            App.navigation.append("app_main")
            App.sm.current = 'sing_in'
    

    def try_logging(self):
        
        headers = {'Content-type': 'application/x-www-form-urlencoded',
        'Accept': 'text/plain'}
        
        req_body = App.tpv_config["credentials"]
        url = os.path.join(App.url_main, "logging", "try_logging") 
        params = urllib.parse.urlencode(req_body)
         
        UrlRequest(url=url,
                  req_body=params,
                  on_success=self.on_success,
                  on_failure=self.on_error,
                  on_error=self.on_error,
                  req_headers=headers)
               

    def on_success(self, v, res):
        if res["success"] == True:
            App.sm.transition.direction = 'right'
            App.sm.current = 'app_main'
            if platform == 'android':
                from android import AndroidService
                service = AndroidService('my pong service', 'running')
                service.start('service started')
                self.service = service
            else:
                from runpy import run_path
                from threading import Thread
                self.service = Thread(
                    target=run_path,
                    args=['service/server.py'],
                    kwargs={'run_name': '__main__'},
                    daemon=True
                )
                self.service.start()
                self.run_service()
                
            

    def run_service(self):
        self.server = server = OSCThreadServer()
        server.listen(
            address=b'localhost',
            port=App.client_port,
            default=True,
        )

        server.bind(b'/message', self.display_message)
        server.bind(b'/date', self.date)

        self.client = OSCClient(b'localhost', App.server_port)
        
    
    def date(self, message):
        print(message)


    def display_message(self, message):
        print(message)


    def on_error(self, v, res):
        if res["success"] == False:
            App.sm.transition.direction = 'left'
            App.navigation.append("app_main")
            App.sm.current = 'sing_in'

    def on_error(self, v, error):
        App.sm.transition.direction = 'left'
        App.navigation.append("app_main")
        App.sm.current = 'sing_in'



    def on_pause(self):
        return True

    def on_stop(self):
        App.is_running = False
        return super().on_stop()

    def on_start(self):
        App.is_running = True
        return super().on_start()

    

if __name__ == "__main__":


    
    with open("config.json", 'r') as app_config:
        data = json.load(app_config)
        App.tpv_config = data
        App.url_main = data["url_main"]
        App.server_port = data["server_port"]
        App.client_port = data["client_port"]
        App.url_ws = data["url_ws"]
    ValleTPVAPP().run()