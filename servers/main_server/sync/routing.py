from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path(r'ws/sync/<params>/', consumers.SyncConsumer),
]