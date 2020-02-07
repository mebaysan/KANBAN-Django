from django.urls import path
from gorev import views

app_name = 'gorev'

urlpatterns = [
    path('gorev_ekle/<slug:proje_slug>/', views.gorev_ekle, name='gorev_ekle'),
    path('detay/<slug:gorev_slug>/', views.gorev_detay, name='gorev_detay'),
    path('not_ekle/<slug:gorev_slug>/', views.not_ekle, name='not_ekle'),
    path('islem_ekle/<slug:gorev_slug>/', views.islem_ekle, name='islem_ekle'),
]
