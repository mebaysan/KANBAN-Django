from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from gorev.models import Gorev
from proje.models import Proje


@login_required
def proje_detay(request, proje_slug):
    proje = Proje.objects.get(slug=proje_slug)
    gorevler = Gorev.objects.filter(proje=proje)
    dosyalar = []
    for gorev in gorevler:
        for dosya in gorev.dosyalar.all():
            dosyalar.append(dosya)
    context = {
        'proje': proje,
        'gorevler': gorevler,
        'dosyalar': dosyalar,
    }
    return render(request, 'proje/proje_detay.html', context=context)
