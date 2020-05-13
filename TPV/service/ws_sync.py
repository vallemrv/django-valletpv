
import websocket
import threading
import time
import os

class WSSync(object):
    def __init__(self, url_ws, url_sync, **kwargs):
        self.message = None
        self.error = None
        self.close = None
        self.open = None
        for k, v in kwargs.items():
            setattr(self, k, v)

        websocket.enableTrace(True)
        self.url_ws = url_ws
        self.url_sync = url_sync
        self.is_running = True
        self.ws = websocket.WebSocketApp(os.path.join(self.url_ws, self.url_sync),
                                on_message = self.on_message,
                                on_error = self.on_error,
                                on_close = self.on_close,)
        self.ws.on_open = self.on_open
        threading.Thread(target=self.run_ws).start()
        
    def run_ws(self):
        while self.is_running:
            time.sleep(0.2)
            self.ws.run_forever()

    def on_message(self, message):
        if self.message:
            self.message(message)

    def on_error(self, error):
        if self.error:
            self.error(ws, error)


    def on_close(self):
        print("close")
        if self.close:
            self.message(ws)

    def on_open(self):
        print("is open")
        if self.open:
            self.open(self.ws)


