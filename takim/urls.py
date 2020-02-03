from django.urls import path
from takim import views

app_name = 'takim'

urlpatterns = [
    path('detay/<str:takim_adi>/', views.takim_detay, name='takim_detay'),
]
