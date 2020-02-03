from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404, reverse

from kanban.local_settings import BASE_URL
from takim.models import Takim
from proje.models import Proje
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from kullanici.models import Kullanici
from django.contrib import messages
import hashlib
from kanban import settings


# Create your views here.


@login_required
def takim_detay(request, takim_slug):
    takim = get_object_or_404(Takim, slug=takim_slug)
    projeler = Proje.objects.filter(takim=takim)
    uyeler = takim.uyeler.all()
    context = {
        'takim': takim,
        'projeler': projeler,
        'uyeler': uyeler
    }
    return render(request, 'takim/takim_detay.html', context=context)


@login_required
@require_http_methods(['POST'])
def takim_olustur(request):
    try:
        _ad = request.POST.get('ad')
        _aciklama = request.POST.get('aciklama')
        yeni_takim = Takim(ad=_ad, aciklama=_aciklama, sahip=request.user)  # bir Takım instance oluşturduk
        yeni_takim.save()
        request.user.takimlar.add(yeni_takim)  # kullanıcının oluşturduğu takımın üyeleri arasına kullanıcıyı ekledik
        request.user.save()
        messages.success(request, 'Takım başarıyla oluşturuldu')
    except:
        messages.warning(request, 'Takım oluşturulurken bir hata oluştu lütfen bir daha deneyin')
    return redirect('kullanici:kullanici')


@login_required
@require_http_methods(['POST'])
def takim_uye_ekle(request, takim_slug):
    email = request.POST.get('email')
    try:
        kullanici = Kullanici.objects.get(email=email)  # gelen epostaya sahip kullanıcı var mı
    except:
        messages.warning(request, 'Bu eposta adresi sisteme kayıtlı olmadığından işlem gerçekleştirilemedi')
        return redirect(reverse('takim:takim_detay', kwargs={'takim_slug': takim_slug}))
    takim = Takim.objects.get(slug=takim_slug)
    token = hashlib.sha256("{}".format(takim_slug).encode('utf-8')).hexdigest()
    kullanici.invite_token = token
    kullanici.save()
    link = BASE_URL + reverse('takim:takim_uye_ekle_onay', kwargs={'takim_slug': takim_slug, 'token': token})
    konu = 'Takım Davetiyesi Hakkında'
    mesaj = 'Sayın {}, {} takımına katılmak için davet aldınız. \nLink:\t{}'.format(
        kullanici.username, takim.ad, link)
    gonderen = settings.EMAIL_HOST_USER
    giden = [kullanici.email]
    send_mail(konu, mesaj, gonderen, giden)
    messages.success(request, 'Davetiye linki başarıyla gönderildi.')
    return redirect(reverse('takim:takim_detay', kwargs={'takim_slug': takim_slug}))


@login_required
def takim_uye_ekle_onay(request, takim_slug, token):
    takim = Takim.objects.get(slug=takim_slug)
    kullanici = Kullanici.objects.get(invite_token=token)
    kullanici.takimlar.add(takim)
    kullanici.save()
    return redirect(reverse('takim:takim_detay', kwargs={'takim_slug': takim_slug}))
