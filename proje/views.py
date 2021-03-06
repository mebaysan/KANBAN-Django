from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponse, JsonResponse
# Create your views here.
from gorev.models import Gorev, GorevGrubu
from kullanici.models import Kullanici
from proje.models import Proje, ProjeDosya
from takim.models import Takim
from aktivite.models import Aktivite
from django.conf import settings
from django.http import HttpResponse, Http404
import os


@login_required
def proje_detay(request, proje_slug):
    proje = get_object_or_404(Proje, slug=proje_slug)
    yapilacaklar = proje.gorevler.filter(gorev_durum='yapilacak').order_by('bitis_tarihi')
    yapilanlar = proje.gorevler.filter(gorev_durum='devam').order_by('bitis_tarihi')
    bitenler = proje.gorevler.filter(gorev_durum='bitti')
    dosyalar = ProjeDosya.objects.filter(proje=proje)
    aktiviteler = Aktivite.objects.filter(proje=proje).order_by(
        '-olusturulma_tarihi')  # en yeniden eskiye doğru sıralar
    context = {
        'proje': proje,
        'dosyalar': dosyalar,
        'yapilacaklar': yapilacaklar,
        'yapilanlar': yapilanlar,
        'bitenler': bitenler,
        'aktiviteler': aktiviteler
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
    uyeler = request.POST.getlist('uyeler')  # bize liste olarak geldiği için
    yeni_proje = Proje(ad=ad, aciklama=aciklama, baslama_tarihi=baslangic_tarih, bitis_tarihi=bitis_tarih,
                       takim=Takim.objects.get(slug=takim_slug))
    yeni_proje.save()
    yeni_aktivite = Aktivite(proje=yeni_proje, kullanici=request.user, aktivite_tipi='olusturma',
                             aktivite="{} adlı projeyi oluşturdu".format(yeni_proje.ad))
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
    yapilacaklar = proje.gorevler.filter(gorev_durum='yapilacak').order_by('bitis_tarihi')
    yapilanlar = proje.gorevler.filter(gorev_durum='devam').order_by('bitis_tarihi')
    bitenler = proje.gorevler.filter(gorev_durum='bitti')
    context = {
        'proje': proje,
        'yapilacaklar': yapilacaklar,
        'yapilanlar': yapilanlar,
        'bitenler': bitenler
    }
    return render(request, 'proje/proje_kanban_board.html', context=context)


@login_required
def proje_dosya_ekle(request, proje_slug):
    proje = Proje.objects.get(slug=proje_slug)
    dosyalar = request.FILES.getlist('file')
    flag = True
    for dosya in dosyalar:
        try:
            proje_dosyasi = ProjeDosya(dosya=dosya, yukleyen=request.user, proje=proje, content_type=dosya.content_type)
            proje_dosyasi.save()
            yeni_islem = Aktivite(proje=proje, kullanici=request.user, aktivite_tipi='ekleme',
                                  aktivite="{} adlı dosyayı ekledi".format(proje_dosyasi.ad))
            yeni_islem.save()
        except:
            flag = False
    if flag:
        messages.success(request, "Dosyalar başarıyla eklendi")
        return JsonResponse({'data': True})
    else:
        return JsonResponse({'data': False})


@login_required
def proje_dosya_indir(request, dosya_slug):
    dosya = ProjeDosya.objects.get(slug=dosya_slug)
    if os.path.exists(dosya.dosya.path):
        with open(dosya.dosya.path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="{}".format(dosya.content_type))
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(dosya.ad)
            return response
    raise Http404


@login_required
def proje_dosya_sil(request, dosya_slug):
    dosya = ProjeDosya.objects.get(slug=dosya_slug)
    dosya.delete()
    yeni_aktivite = Aktivite(proje=dosya.proje, kullanici=request.user, aktivite_tipi='silme',
                             aktivite="{} adlı dosyayı sildi".format(dosya.ad))
    yeni_aktivite.save()
    messages.success(request, 'Dosya başarıyla silindi')
    return redirect(reverse('proje:proje_detay', kwargs={'proje_slug': dosya.proje.slug}))


@login_required
def proje_ajax_islemler(request):
    if request.method == 'POST' and request.is_ajax():  # eğer gelen istek ajax ve POST ise dedik
        islem_tipi = request.POST.get('islem_tipi')  # ajax kısmında yolladığımız form_data içerisinden alıyoruz
        if islem_tipi == 'proje_detay_getir':
            proje = Proje.objects.get(slug=request.POST.get('proje_slug'))
            return JsonResponse(
                {'proje_adi': proje.ad, 'proje_aciklama': proje.aciklama, 'baslangic_tarihi': proje.baslama_tarihi,
                 'bitis_tarihi': proje.bitis_tarihi, 'proje_slug': proje.slug})
        elif islem_tipi == 'proje_guncelle':
            proje = Proje.objects.get(slug=request.POST.get('proje_slug'))
            proje.ad = request.POST.get('proje_ad')
            proje.aciklama = request.POST.get('proje_aciklama')
            proje.baslama_tarihi = request.POST.get('proje_baslangic')
            proje.bitis_tarihi = request.POST.get('proje_bitis')
            proje.save()
            messages.success(request, 'Proje başarıyla güncellendi')
            return JsonResponse({'success': True})


def handler404(request, exception):
    return render(request, 'utilities/404.html', locals())
