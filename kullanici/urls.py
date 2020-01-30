from django.urls import path
from kullanici import views

app_name = 'kullanici'

urlpatterns = [
    path('kayit_ol/', views.kayit_ol, name='kayit_ol'),
    path('giris_yap/', views.giris_yap, name='giris_yap'),
    path('cikis_yap/', views.cikis_yap, name='cikis_yap'),
    path('profile/<str:kname>/', views.profile, name='profile'),
]
