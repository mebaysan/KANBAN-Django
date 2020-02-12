from django.db import models
import os
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe

from kullanici.models import Kullanici
from takim.models import Takim


class Proje(models.Model):
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    baslama_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    takim = models.ForeignKey(Takim, related_name='projeler', on_delete=models.SET_NULL, null=True)
    uyeler = models.ManyToManyField(to='kullanici.Kullanici', related_name='projeler', null=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.ad

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.ad))
        new_slug = slug
        while Proje.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            proje = Proje.objects.get(slug=self.slug)
            if proje.ad != self.ad:
                self.slug = self.get_unique_slug()
        super(Proje, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.


class ProjeDosya(models.Model):
    proje = models.ForeignKey(to='proje.Proje', related_name='dosyalar', on_delete=models.SET_NULL, null=True)
    dosya = models.FileField(upload_to='projeler/dosyalar/')
    yukleyen = models.ForeignKey(to='kullanici.Kullanici', related_name='proje_dosyalari', on_delete=models.CASCADE)
    ad = models.CharField(max_length=255, blank=True)
    content_type = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    class Meta:
        verbose_name = 'Proje Dosyası'
        verbose_name_plural = 'Proje Dosyaları'

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.ad))
        new_slug = slug
        while ProjeDosya.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def __str__(self):
        return self.ad

    def save(self, *args, **kwargs):  # save edilmeden önce,
        self.ad = os.path.basename(
            self.dosya.name)  # basename fonksiyonu ile içine verdiğimiz pathin (dosya.name) dosya adını verir
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            proje_dosya = ProjeDosya.objects.get(slug=self.slug)
            if proje_dosya.ad != self.ad:
                self.slug = self.get_unique_slug()

        super(ProjeDosya, self).save(*args, **kwargs)
