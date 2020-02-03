from django.urls import path
from proje import views

app_name = 'proje'

urlpatterns = [
    path('detay/<slug:proje_slug>', views.proje_detay, name='proje_detay'),
]
