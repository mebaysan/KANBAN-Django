from django.urls import path
from proje import views

app_name = 'proje'

urlpatterns = [
    path('detay/<str:proje_adi>', views.proje_detay, name='proje_detay'),
]
