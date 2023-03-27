from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path('wastebins/', views.wastebins, name="wastebins"),
path('wastebins-chartdata/', views.neighbourhood_chartdata, name='neighbourhood-chartdata'),
path('wastebins-tabledata/', views.neighbourhood_tabledata, name='neighbourhood-tabledata'),
]