from django.shortcuts import render
from proje.models import Proje


# Create your views here.


def index(request):
    proje = Proje.objects.first()
    gorev = proje.gorevler.first()
    islem = gorev.islemler.first()
    note = gorev.notlar.first()
    dosya = gorev.dosyalar.first()
    context = {
        'proje': proje,
        'gorev': gorev,
        'islem': islem,
        'not': note,
        'dosya': dosya,
    }
    return render(request, 'index.html', context=context)
