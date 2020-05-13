import os
import socket
from threading import Thread, _start_new_thread
from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.screenmanager import Screen
from kivy.properties import  StringProperty, BooleanProperty

KVS_FILES = os.environ["KVS_FILES"]
Builder.load_file(KVS_FILES+"/findserver.kv")

class FindServer(Screen):
    button_caption = StringProperty("Buscar servidor")
    button_disable = BooleanProperty(False)


    def find_server(self):
        self.button_caption = "Buscando...."
        self.button_disable = True
        Thread(target=self.find_server_th).start()
        

    def find_server_th(self):
        import time
        def thr(ip_address):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            message = "Servidor no encontrado ip "+ ip_address
            if App.stopped:
                s.close()
                return
            else:
                conn = s.connect_ex((ip_address, 3434))
                if conn == 0:
                    message="Servidor encontrado ip "+ ip_address
                    s.close()
            print(message)
                

        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        print("buscando.....")
        preffix = ip_address.split(".")[0:3]

        for i in range(2, 256):
            if App.stopped:
                return
            ip_address = ".".join(preffix + [str(i)])
            print(ip_address)
            Thread(target=thr, args=(ip_address,)).start()
            
       