from django.urls import path
from takim import views

app_name = 'takim'

urlpatterns = [
    path('detay/<slug:takim_slug>/', views.takim_detay, name='takim_detay'),
]
