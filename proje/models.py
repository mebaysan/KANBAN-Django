from django.db import models

from unidecode import unidecode
from django.template.defaultfilters import slugify, safe

from kullanici.models import Kullanici
from takim.models import Takim


class Proje(models.Model):
    gizlilik_secenekleri = (
        ('herkese_acik', 'Herkese Açık'),
        ('takim_uyeleri', 'Sadece Takım Üyeleri'),
        ('sadece_ben', 'Sadece Ben')
    )
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)
    baslama_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    gizlilik = models.CharField(max_length=25, choices=gizlilik_secenekleri)
    takim = models.ForeignKey(Takim, related_name='projeler', on_delete=models.SET_NULL, null=True)
    uyeler = models.ManyToManyField(to='kullanici.Kullanici',related_name='projeler',null=True)
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