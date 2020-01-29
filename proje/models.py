from django.db import models
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

    class Meta:
        verbose_name = 'Proje'
        verbose_name_plural = 'Projeler'

    def __str__(self):
        return self.ad
