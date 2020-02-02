from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from kullanici.models import Kullanici
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail
from django.conf import settings


def kayit_ol(request):
    if request.method == 'POST':
        gelen_veri = {
            'email': request.POST['email'],
            'username': request.POST['username'],
            'password': request.POST['password'],
            'password_check': request.POST.get('password_check'),
        }
        if len(Kullanici.objects.filter(username=gelen_veri['username'])) == 0 and len(
                Kullanici.objects.filter(email=gelen_veri['email'])) == 0:
            kullanici = Kullanici(username=gelen_veri['username'], email=gelen_veri['email'])
            kullanici.set_password(gelen_veri['password'])
            kullanici.save()
            messages.success(request, 'Başarıyla Kayıt Oldunuz...')
            return redirect('kullanici:giris_yap')
        else:
            messages.warning(request,
                             'Kullanıcı Adı ({}) veya Eposta Adresi ({}) kayıtlı olduğundan kayıt işlemi iptal edildi...'.format(
                                 gelen_veri['username'], gelen_veri['email']))
            return redirect('kullanici:kayit_ol')
    return render(request, 'kullanici/kayit_ol.html')


def giris_yap(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)  # user'i doğruladık
        if user != None:  # eğer user nesnesi varsa
            login(request, user)  # login yaptık
            messages.success(request, 'Sayın {} başarıyla giriş yaptınız'.format(username))
            return redirect('kullanici:kullanici')
        else:
            messages.warning(request, 'Kullanıcı bulunamadığından giriş yapılamadı.')
            return redirect('kullanici:giris_yap')
    return render(request, 'kullanici/giris_yap.html')


@login_required
def cikis_yap(request):
    username = request.user.username
    logout(request)
    messages.success(request, 'Sayın {},Başarıyla çıkış yapıldı.'.format(username))
    return redirect('kullanici:giris_yap')


@login_required
def kullanici(request):
    kullanici = request.user
    context = {
        'kullanici': kullanici
    }
    return render(request, 'kullanici/profile.html', context=context)


@login_required
@require_http_methods(['POST'])
def kullanici_guncelle(request):
    kullanici = request.user
    ad = request.POST.get('ad')
    soyad = request.POST.get('soyad')
    email = request.POST.get('email')
    lokasyon = request.POST.get('lokasyon')
    bio = request.POST.get('bio')
    try:
        profil_foto = request.FILES['profil_foto']  # post edilen datadan fotoğrafı al
    except:
        profil_foto = kullanici.profil_foto  # eğer alamazsan gelmemiş demektir o zaman profil_foto değişkenini mevcut kullanıcının profil_foto'su ile set et
    if not ad: ad = request.user.first_name  # eğer ad değişkeni yoksa, ad değişkenini oluştur ve değerini set et
    if not soyad: soyad = request.user.last_name
    if not email: email = request.user.email
    if not lokasyon: lokasyon = request.user.lokasyon
    if not bio: bio = request.user.bio
    kullanici.first_name = ad
    kullanici.last_name = soyad
    kullanici.email = email
    kullanici.lokasyon = lokasyon
    kullanici.bio = bio
    kullanici.profil_foto = profil_foto
    kullanici.save()
    messages.success(request, 'Sayın {}, Profiliniz başarıyla güncellendi.'.format(request.user.username))
    return redirect('kullanici:kullanici')


@login_required
@require_http_methods(['POST'])
def kullanici_sifre_guncelle(request):
    kullanici = request.user
    yeni_sifre = request.POST.get('yeni_sifre')
    kullanici.set_password(yeni_sifre)
    kullanici.save()
    konu = 'Şifre Güncellemesi Hakkında'
    mesaj = 'Sayın {} şifreniz başarıyla güncellenmiştir. Bu işlemden haberiniz yoksa destek ekip ile irtibata geçmeniz gerekmektedir.'.format(
        kullanici.username)
    gonderen = settings.EMAIL_HOST_USER  # kimden göndereceğimizi settings dosyamız içerisinde belirlediğimiz mail servisimizin HOST_USER'ı olarak belirledik
    giden = [kullanici.email]  # mailin gideceği listeyi LİSTE tipinde vermeliyiz
    send_mail(konu, mesaj, gonderen, giden)  # django'nun mail fonksiyonunu kullanıyoruz
    messages.success(request, 'Sayın {}, Şifreniz başarıyla güncellendi.Yeni şifre ile giriş yapabilirsiniz'.format(
        request.user.username))
    return redirect('kullanici:giris_yap')


def kullanici_sifremi_unuttum(request):
    #toDO: şifremi unuttum view yazılacak!
    messages.success(request, 'Şifrenizi güncellemeniz için gerekli mail tarafınıza iletilmiştir.')
    return redirect('kullanici:giris_yap')
