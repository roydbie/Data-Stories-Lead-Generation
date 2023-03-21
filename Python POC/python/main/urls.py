from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("neighbourhoods/", views.neighbourhoods, name="neighbourhoods"),
path('neighbourhood-chart/', views.neighbourhood_chart, name='neighbourhood-chart'),
path("neighbourhoods/<int:id>", views.neighbourhood, name="neighbourhood")
]