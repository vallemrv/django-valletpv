import json
from base64 import  b64decode

from asgiref.sync import async_to_sync

from channels.generic.websocket import WebsocketConsumer

from django.contrib.auth import authenticate

from .models import Sync


class SyncConsumer(WebsocketConsumer):
   
   def connect(self):    
      params = b64decode(self.scope['url_route']['kwargs']['params'])
      params = json.loads(params)
      self.user = {"pk": params["user"], "token": params["token"]}
      self.model = params["model"]
      self.user = authenticate(pk=self.params["user"], token=self.params['token'])
      if self.user:
         sync = Sync.object.filter(user__pk=self.user.pk)
         if sync.empresa:
            self.room_group_name =  sync.empresa.pk
            self.channel_global = self.model
            self.channel_privado = self.user_token
            async_to_sync(self.channel_layer.group_add)(
               self.room_group_name,
               self.channel_global
            )
            async_to_sync(self.channel_layer.group_add)(
               self.room_group_name,
               self.channel_privado
            )



   def disconnect(self, code):
      async_to_sync(self.channel_layer.group_discard)(
         self.room_group_name,
         self.channel_global
      )
      async_to_sync(self.channel_layer.group_discard)(
         self.room_group_name,
         self.channel_privado
      )
      return super().disconnect(code)


   def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )