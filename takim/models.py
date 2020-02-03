from django.db import models

# Create your models here.

class Takim(models.Model):
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    uyeler = models.ManyToManyField(to='kullanici.Kullanici',related_name='uyeler',null=True)

    class Meta:
        verbose_name = 'Takım'
        verbose_name_plural = 'Takımlar'
    def __str__(self):
        return self.ad