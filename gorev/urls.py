from django.urls import path
from gorev import views

app_name = 'gorev'

urlpatterns = [
    path('gorev_ekle/<slug:proje_slug>/', views.gorev_ekle, name='gorev_ekle'),
    path('detay/<slug:gorev_slug>/', views.gorev_detay, name='gorev_detay'),
    path('detay/<slug:gorev_slug>/dosya/ekle/', views.gorev_dosya_ekle, name='gorev_dosya_ekle'),
    path('not_ekle/<slug:gorev_slug>/', views.not_ekle, name='not_ekle'),
    path('islem_ekle/<slug:gorev_slug>/', views.islem_ekle, name='islem_ekle'),
    path('gorev_sil/<slug:gorev_slug>/', views.gorev_sil, name='gorev_sil'),
    path('gorev/durum/degistir/inprogress/<slug:gorev_slug>/', views.gorev_islem_durum_degistir_yapim_asamasi,
         name='gorev_durum_degistir_inprogress'),
    path('gorev/durum/degistir/done/<slug:gorev_slug>/', views.gorev_islem_durum_degistir_basarili,
         name='gorev_durum_degistir_done'),
    path('dosyalar/indir/<slug:dosya_slug>', views.gorev_dosya_indir, name='gorev_dosya_indir'),
    path('dosyalar/sil/<slug:dosya_slug>', views.gorev_dosya_sil, name='gorev_dosya_sil'),
]
