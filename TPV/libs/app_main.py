import os
from kivy.lang import  Builder
from kivy.app import  App
from kivy.uix.screenmanager import  Screen

KVS_FILES = os.environ["KVS_FILES"]
Builder.load_file(KVS_FILES+"/app_main.kv")

class AppMain(Screen):
    pass