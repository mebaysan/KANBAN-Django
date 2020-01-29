from django.db import models
from kullanici.models import Kullanici
from proje.models import Proje


# Create your models here.


class Gorev(models.Model):
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    baslama_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    proje = models.ForeignKey(Proje, related_name='gorevler', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name= 'Görev'
        verbose_name_plural = 'Görevler'
    def __str__(self):
        return self.ad


class Islem(models.Model):
    islem_sureci_secenekleri = (
        ('bitti', 'İşlem Bitti'),
        ('devam', 'İşlem Devam Ediyor')
    )
    gorev = models.ForeignKey(Gorev, related_name='islemler', on_delete=models.SET_NULL, null=True)
    ad = models.CharField(max_length=255)
    islem_sureci = models.CharField(max_length=5, choices=islem_sureci_secenekleri,default='devam')
    class Meta:
        verbose_name= 'İşlem'
        verbose_name_plural = 'İşlemler'
    def __str__(self):
        return self.ad


class Not(models.Model):
    gorev = models.ForeignKey(Gorev, related_name='notlar', on_delete=models.SET_NULL, null=True)
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    yazar = models.ForeignKey(Kullanici, related_name='notlar', on_delete=models.SET_NULL, null=True)
    class Meta:
        verbose_name= 'Not'
        verbose_name_plural = 'Notlar'
    def __str__(self):
        return self.ad


class Dosya(models.Model):
    gorev = models.ForeignKey(Gorev, related_name='dosyalar', on_delete=models.SET_NULL, null=True)
    ad = models.CharField(max_length=255)
    tip = models.CharField(max_length=255)
    dosya = models.FileField(upload_to='gorevler/dosyalar/')
    class Meta:
        verbose_name= 'Dosya'
        verbose_name_plural = 'Dosyalar'
    def __str__(self):
        return self.ad
