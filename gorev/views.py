from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseForbidden, JsonResponse
# Create your views here.
from gorev.models import Gorev, GorevGrubu, Islem, Not, GorevDosya
from kullanici.models import Kullanici
from proje.models import Proje
from aktivite.models import Aktivite


@login_required
@require_http_methods(['POST'])
def gorev_ekle(request, proje_slug):
    proje = get_object_or_404(Proje, slug=proje_slug)
    ad = request.POST.get('ad')
    aciklama = request.POST.get('aciklama')
    baslama_tarihi = request.POST.get('baslama_tarihi')
    bitis_tarihi = request.POST.get('bitis_tarihi')
    uyeler = request.POST.getlist('uyeler')
    yeni_gorev = Gorev(ad=ad, aciklama=aciklama, baslama_tarihi=baslama_tarihi, bitis_tarihi=bitis_tarihi,
                       proje=Proje.objects.get(slug=proje_slug))
    yeni_gorev.save()
    yeni_aktivite = Aktivite(proje=proje, gorev=yeni_gorev, kullanici=request.user, aktivite_tipi='olusturma',
                             aktivite="{} adlı görevi oluşturdu".format(yeni_gorev.ad))
    yeni_aktivite.save()
    for uye in uyeler:
        obj = Kullanici.objects.get(username=uye)
        yeni_gorev.uyeler.add(obj)
    yeni_gorev.save()
    return redirect(reverse('proje:proje_detay', kwargs={'proje_slug': proje_slug}))


@login_required
def gorev_detay(request, gorev_slug):
    gorev = get_object_or_404(Gorev, slug=gorev_slug)
    islemler = gorev.islemler.all()
    notlar = gorev.notlar.all()
    dosyalar = gorev.dosyalar.all()
    aktiviteler = Aktivite.objects.filter(gorev=gorev).order_by('-olusturulma_tarihi')
    context = {
        'gorev': gorev,
        'islemler': islemler,
        'notlar': notlar,
        'dosyalar': dosyalar,
        'aktiviteler': aktiviteler
    }
    return render(request, 'gorev/gorev_detay.html', context=context)


@login_required
@require_http_methods(['POST'])
def not_ekle(request, gorev_slug):
    gorev = get_object_or_404(Gorev, slug=gorev_slug)
    proje = gorev.proje
    not_adi = request.POST.get('ad')
    not_aciklamasi = request.POST.get('aciklama')
    yeni_not = Not(ad=not_adi, aciklama=not_aciklamasi, kullanici=request.user, gorev=gorev)
    yeni_not.save()
    yeni_aktivite = Aktivite(proje=proje, gorev=gorev, kullanici=request.user, aktivite_tipi='ekleme',
                             aktivite="{} adlı notu ekledi".format(yeni_not.ad))
    yeni_aktivite.save()
    messages.success(request, 'Başarıyla not eklendi')
    return redirect(reverse('gorev:gorev_detay', kwargs={'gorev_slug': gorev_slug}))


@login_required
@require_http_methods(['POST'])
def islem_ekle(request, gorev_slug):
    gorev = get_object_or_404(Gorev, slug=gorev_slug)
    proje = gorev.proje
    islem_adi = request.POST.get('ad')
    islem = Islem(ad=islem_adi)
    islem.save()
    gorev.islemler.add(islem)
    yeni_aktivite = Aktivite(proje=proje, gorev=gorev, kullanici=request.user, aktivite_tipi='ekleme',
                             aktivite="{} adlı işlemi ekledi".format(islem.ad))
    yeni_aktivite.save()
    return redirect(reverse('gorev:gorev_detay', kwargs={'gorev_slug': gorev_slug}))


@login_required
def gorev_dosya_ekle(request, gorev_slug):
    gorev = Gorev.objects.get(slug=gorev_slug)
    dosyalar = request.FILES.getlist('file')
    flag = True
    for dosya in dosyalar:
        try:
            gorev_dosyasi = GorevDosya(dosya=dosya, yukleyen=request.user, gorev=gorev,
                                       content_type=dosya.content_type)
            gorev_dosyasi.save()
            yeni_islem = Aktivite(proje=gorev.proje, gorev=gorev, kullanici=request.user, aktivite_tipi='ekleme',
                                  aktivite="{} adlı dosyayı ekledi".format(gorev_dosyasi.ad))
            yeni_islem.save()
        except:
            flag = False
    if flag:
        messages.success(request, "Dosyalar başarıyla eklendi")
        return JsonResponse({'data': True})
    else:
        return JsonResponse({'data': False})
