from django.shortcuts import render
from takim.models import Takim
from proje.models import Proje
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def takim_detay(request, takim_slug):
    takim = Takim.objects.get(slug=takim_slug)
    projeler = Proje.objects.filter(takim=takim)
    uyeler = takim.uyeler.all()
    context = {
        'takim': takim,
        'projeler':projeler,
        'uyeler':uyeler
    }
    return render(request, 'takim/takim_detay.html', context=context)
