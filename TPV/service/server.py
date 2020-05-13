import time
import json
from service.ws_sync import WSSync
from base64 import  b64encode
from kivy.app import  App

from oscpy.server import OSCThreadServer
from oscpy.client import OSCClient

from ..models.models import Sync



CLIENT = OSCClient('localhost', App.client_port)


def ping(*_):
    'answer to ping messages'
    CLIENT.send_message(
        b'/message',
        [],
    )


def send_date():
    'send date to the application'
    CLIENT.send_message(
        b'/date',
        [],
    )

def on_open(ws):
    ws.send({'op': 'sync'})
    


if __name__ == '__main__':
    SERVER = OSCThreadServer()
    SERVER.listen('localhost', port=App.server_port, default=True)
    SERVER.bind(b'/ping', ping)
    url_params = b64encode(json.dumps(App.tpv_config["credentials"]).encode())
    url_params["model"] = "modelo"
    sync = WSSync(App.url_ws, url_params.decode(), open=on_open)
    