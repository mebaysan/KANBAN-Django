from django.db import models


# Create your models here.

class Takim(models.Model):
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()

    class Meta:
        verbose_name = 'Takım'
        verbose_name_plural = 'Takımlar'
    def __str__(self):
        return self.ad