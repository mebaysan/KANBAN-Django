from django.urls import path
from takim import views

app_name = 'takim'

urlpatterns = [
    path('detay/<slug:takim_slug>/', views.takim_detay, name='takim_detay'),
    path('olustur/', views.takim_olustur, name='takim_olustur'),
    path('sil/<slug:takim_slug>/', views.takimi_sil, name='takim_sil'),
    path('ayril/<slug:takim_slug>/', views.takimdan_ayril, name='takim_ayril'),
    path('ajax/islemler/', views.takim_ajax_islemler, name='takim_ajax_islemler'),
    path('uye_ekle/<slug:takim_slug>/', views.takim_uye_ekle, name='takim_uye_ekle'),
    path('uye_ekle/onay/<slug:takim_slug>/<str:token>/', views.takim_uye_ekle_onay, name='takim_uye_ekle_onay'),
]
