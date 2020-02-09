from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseForbidden
# Create your views here.
from gorev.models import Gorev, GorevGrubu
from kullanici.models import Kullanici
from proje.models import Proje, ProjeDosya
from takim.models import Takim
from aktivite.models import Aktivite


@login_required
def proje_detay(request, proje_slug):
    proje = get_object_or_404(Proje, slug=proje_slug)
    yapilacaklar = proje.gorevler.filter(gorev_durum='yapilacak')
    yapilanlar = proje.gorevler.filter(gorev_durum='devam')
    bitenler = proje.gorevler.filter(gorev_durum='bitti')
    dosyalar = ProjeDosya.objects.filter(proje=proje)
    context = {
        'proje': proje,
        'dosyalar': dosyalar,
        'yapilacaklar': yapilacaklar,
        'yapilanlar': yapilanlar,
        'bitenler': bitenler
    }
    return render(request, 'proje/proje_detay.html', context=context)


@login_required
@require_http_methods(['POST'])
def proje_ekle(request, takim_slug):
    if request.user != Takim.objects.get(slug=takim_slug).sahip:
        return HttpResponseForbidden()
    ad = request.POST.get('ad')
    aciklama = request.POST.get('aciklama')
    baslangic_tarih = request.POST.get('baslangic_tarih')
    bitis_tarih = request.POST.get('bitis_tarih')
    gizlilik = request.POST.get('gizlilik')
    uyeler = request.POST.getlist('uyeler')  # bize liste olarak geldiği için
    yeni_proje = Proje(ad=ad, aciklama=aciklama, baslama_tarihi=baslangic_tarih, bitis_tarihi=bitis_tarih,
                       gizlilik=gizlilik, takim=Takim.objects.get(slug=takim_slug))
    yeni_proje.save()
    yeni_aktivite = Aktivite(proje=yeni_proje, kullanici=request.user, aktivite_tipi='olusturma',
                             aktivite="{}, {} adlı projeyi oluşturdu".format(request.user.username, yeni_proje.ad))
    yeni_aktivite.save()
    for uye in uyeler:
        obj = Kullanici.objects.get(email=uye)
        yeni_proje.uyeler.add(obj)
    yeni_proje.save()
    messages.success(request, 'Proje başarıyla oluşturuldu.')
    return redirect(reverse('takim:takim_detay', kwargs={'takim_slug': takim_slug}))


@login_required
def proje_kanban_board(request, proje_slug):
    proje = get_object_or_404(Proje, slug=proje_slug)
    yapilacaklar = proje.gorevler.filter(gorev_durum='yapilacak')
    yapilanlar = proje.gorevler.filter(gorev_durum='devam')
    bitenler = proje.gorevler.filter(gorev_durum='bitti')
    context = {
        'proje': proje,
        'yapilacaklar': yapilacaklar,
        'yapilanlar': yapilanlar,
        'bitenler': bitenler
    }
    return render(request, 'proje/proje_kanban_board.html', context=context)
