from django.urls import path

from . import views

urlpatterns = [
    path("sing_up", views.sing_up, name="sing_up"),
    path("try_logging", views.test_logging, name="try_logging")
]
