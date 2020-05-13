import json
import os
import  urllib
from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.screenmanager import  Screen
from kivy.network.urlrequest import  UrlRequest
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.clock import  Clock


from kivymd.uix.snackbar import Snackbar

KVS_FILES = os.environ["KVS_FILES"]
Builder.load_file(KVS_FILES+"/sing_up.kv")

class SingUp(Screen):
    
    def send_data(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded',
          'Accept': 'text/plain'}
        
        req_body = {
            'first_name': self.ids.first_name.text,
            'password': self.ids.password.text,
            'username': self.ids.username.text,
         }
        url = App.url_main+"/logging/sing_up"
        params = urllib.parse.urlencode(req_body)
        UrlRequest(url=url,
                  req_body=params,
                  on_success=self.on_success,
                  req_headers=headers)
                  

    def on_success(self, v, res):
        if res["success"] == False:
            Snackbar(text="Username escogido").show()
        else:
            Snackbar(text="Registro exitoso").show()
            Clock.schedule_once(self.cancel, 0.5)


    def pass_not_match(self):
        Snackbar(text="Las contraseñas no coinciden").show()

    def singup(self):
        self.send_data()

    def cancel(self, dt=0):
        self.manager.transition.direction = 'right' 
        self.manager.current =  App.navigation.pop()


    