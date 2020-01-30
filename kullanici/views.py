from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from kullanici.models import Kullanici
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
            return redirect(reverse('kullanici:profile', kwargs={'kname': user.username}))
        else:
            messages.warning(request, 'Kullanıcı bulunamadığından giriş yapılamadı.')
            return redirect('kullanici:giris_yap')
    return render(request, 'kullanici/giris_yap.html')


@login_required
def cikis_yap(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yapıldı.')
    return redirect('kullanici:giris_yap')


@login_required
def profile(request, kname):
    kullanici = Kullanici.objects.get(username=kname)
    context = {
        'kullanici': kullanici
    }
    return render(request, 'kullanici/profile.html', context=context)
