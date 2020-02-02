from django.urls import path
from kullanici import views

app_name = 'kullanici'

urlpatterns = [
    path('kayit_ol/', views.kayit_ol, name='kayit_ol'),
    path('giris_yap/', views.giris_yap, name='giris_yap'),
    path('cikis_yap/', views.cikis_yap, name='cikis_yap'),
    path('profil/', views.kullanici, name='kullanici'),
    path('guncelle/', views.kullanici_guncelle, name='kullanici_guncelle'),
    path('sifre/guncelle', views.kullanici_sifre_guncelle, name='kullanici_sifre_guncelle'),
    path('sifre/sifremi-unuttum', views.kullanici_sifremi_unuttum, name='kullanici_sifremi_unuttum'),
    path('sifre/sifremi-unuttum/onay/<str:hash>', views.kullanici_sifremi_unuttum_onay, name='kullanici_sifremi_unuttum_onay'),
]
