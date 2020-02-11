from django.urls import path
from proje import views

app_name = 'proje'

urlpatterns = [
    path('detay/<slug:proje_slug>', views.proje_detay, name='proje_detay'),
    path('<slug:takim_slug>/ekle/', views.proje_ekle, name='proje_ekle'),
    path('<slug:proje_slug>/dosya/ekle/', views.proje_dosya_ekle, name='proje_dosya_ekle'),
    path('kanban/board/<slug:proje_slug>/', views.proje_kanban_board, name='kanban_board'),
    path('ajax/islemler', views.proje_ajax_islemler, name='proje_ajax_islemler'),
]
