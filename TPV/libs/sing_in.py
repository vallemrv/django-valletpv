import json
import os
import  urllib
from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.screenmanager import  Screen
from kivy.network.urlrequest import  UrlRequest
from kivy.properties import ObjectProperty
from kivy.core.window import Window

from kivymd.uix.snackbar import Snackbar

KVS_FILES = os.environ["KVS_FILES"]
Builder.load_file(KVS_FILES+"/sing_in.kv")

class SingIn(Screen):

    def get_data(self):
        headers = {'Content-type': 'application/x-www-form-urlencoded',
          'Accept': 'text/plain'}
        
        req_body = {
            'username': self.ids.username.text,
            'password': self.ids.password.text
        }
        url = os.path.join(App.url_main, "token","new.json") 
        params = urllib.parse.urlencode(req_body)
         
        UrlRequest(url=url,
                  req_body=params,
                  on_success=self.on_success,
                  on_failure=self.on_error,
                  req_headers=headers)
               

    def on_success(self, v, res):
        if res["success"] == False:
            Snackbar(text="Usuario o contraseña no validas").show()
        else:
            Snackbar(text="Registro exitoso").show()
            with open("config.json", 'w') as app_config:
                App.tpv_config["credentials"] = res
                app_config.write(json.dumps(App.tpv_config))
            self.manager.transition.direction = 'right' 
            self.manager.current =  App.navigation.pop()

            
                

    def on_error(self, v, res):
        if res["success"] == False:
            Snackbar(text="Usuario o contraseña no validas").show()
        else:
            Snackbar(text="Usuario perfect").show()

  
    def sing_up(self):
        self.manager.transition.direction = 'left'
        App.navigation.append(self.name)
        self.manager.current = 'sing_up'

    def loggin(self):
        self.get_data()
       

    def recover_pass(self):
        Snackbar(text="Aún no implementado").show()