from django.urls import path
from takim import views

app_name = 'takim'

urlpatterns = [
    path('', views.index, name='index'),
]
