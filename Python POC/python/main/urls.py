from django.urls import path

from . import views

urlpatterns = [
path("", views.home, name="home"),
path('wastebins/', views.wastebins, name="wastebins"),
path('wastebins_chartdata/', views.wastebins_chartdata, name='wastebins_chartdata'),
path('wastebins_tabledata/', views.wastebins_tabledata, name='wastebins_tabledata'),

path('publicreports/', views.publicreports, name="publicreports"),
path('publicreports_data/x=<x>&y=<y>', views.publicreports_data, name='publicreports_data'),
]