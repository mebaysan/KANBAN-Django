from django.urls import path
from kullanici import views

app_name = 'kullanici'

urlpatterns = [
    path('kayit_ol/', views.kayit_ol, name='kayit_ol'),
    path('giris_yap/', views.giris_yap, name='giris_yap'),
    path('cikis_yap/', views.cikis_yap, name='cikis_yap'),
    path('kullanici/', views.kullanici, name='kullanici'),
    path('kullanici/guncelle/', views.kullanici_guncelle, name='kullanici_guncelle'),
    path('kullanici/guncelle/sifre', views.kullanici_sifre_guncelle, name='kullanici_sifre_guncelle'),
]
