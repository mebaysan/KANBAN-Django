import os

from django.db import models
from kullanici.models import Kullanici
from proje.models import Proje

from unidecode import unidecode
from django.template.defaultfilters import slugify, safe


# Create your models here.

class GorevGrubu(models.Model):
    ad = models.CharField(max_length=255, null=True, blank=False)
    proje = models.ForeignKey(to='proje.Proje', related_name='gorev_gruplari', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Görev Grubu'
        verbose_name_plural = 'Görev Grupları'

    def __str__(self):
        return self.ad

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.ad))
        new_slug = slug
        while GorevGrubu.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            gorev_grubu = GorevGrubu.objects.get(slug=self.slug)
            if gorev_grubu.ad != self.ad:
                self.slug = self.get_unique_slug()
        super(GorevGrubu, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.


class Gorev(models.Model):
    gorev_durumlari = (
        ('bitti', 'Görev Bitti'),       # Done
        ('devam', 'Görev Devam Ediyor'), # InProgress
        ('yapilacak','Görev Yapılmalı') # ToDos
    )
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    baslama_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    gorev_durum = models.CharField(max_length=11, choices=gorev_durumlari, default='yapilacak')
    proje = models.ForeignKey(Proje, related_name='gorevler', on_delete=models.SET_NULL, null=True)
    uyeler = models.ManyToManyField(to='kullanici.Kullanici', related_name='gorevler', null=True)
    #gorev_grubu = models.ForeignKey(to='gorev.GorevGrubu', related_name='gorevler', null=True, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Görev'
        verbose_name_plural = 'Görevler'

    def __str__(self):
        return self.ad

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.ad))
        new_slug = slug
        while Gorev.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            gorev = Gorev.objects.get(slug=self.slug)
            if gorev.ad != self.ad:
                self.slug = self.get_unique_slug()
        super(Gorev, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.


class Islem(models.Model):
    islem_sureci_secenekleri = (
        ('bitti', 'İşlem Bitti'),
        ('devam', 'İşlem Devam Ediyor')
    )
    gorev = models.ForeignKey(Gorev, related_name='islemler', on_delete=models.SET_NULL, null=True)
    ad = models.CharField(max_length=255)
    islem_sureci = models.CharField(max_length=5, choices=islem_sureci_secenekleri, default='devam')
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,null=True)

    class Meta:
        verbose_name = 'İşlem'
        verbose_name_plural = 'İşlemler'

    def __str__(self):
        return self.ad


class Not(models.Model):
    gorev = models.ForeignKey(Gorev, related_name='notlar', on_delete=models.SET_NULL, null=True)
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    kullanici = models.ForeignKey(Kullanici, related_name='notlar', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Not'
        verbose_name_plural = 'Notlar'

    def __str__(self):
        return self.ad


class GorevDosya(models.Model):
    gorev = models.ForeignKey(to='gorev.Gorev', related_name='dosyalar', on_delete=models.SET_NULL, null=True)
    dosya = models.FileField(upload_to='gorevler/dosyalar/')
    ad = models.CharField(max_length=255, blank=True)
    yukleyen = models.ForeignKey(to='kullanici.Kullanici',related_name='gorev_dosyalari',on_delete=models.CASCADE)
    content_type = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Görev Dosyası'
        verbose_name_plural = 'Görev Dosyaları'

    def __str__(self):
        return self.gorev.ad

    def save(self, *args, **kwargs):
        self.ad = os.path.basename(self.dosya.name)
        super(GorevDosya, self).save(*args, **kwargs)
