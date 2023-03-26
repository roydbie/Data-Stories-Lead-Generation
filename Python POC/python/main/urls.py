from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path("neighbourhoods/", views.neighbourhoods, name="neighbourhoods"),
path('neighbourhood-chartdata/', views.neighbourhood_chartdata, name='neighbourhood-chart'),
path('neighbourhood-data/', views.neighbourhood_data, name='neighbourhood-data'),
path("neighbourhoods/<int:id>", views.neighbourhood, name="neighbourhood")
]