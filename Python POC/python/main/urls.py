from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("neighbourhoods/", views.neighbourhoods, name="neighbourhoods"),
path("neighbourhoods/<int:id>", views.neighbourhood, name="neighbourhood")
]