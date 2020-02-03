from django.db import models
from unidecode import unidecode
from django.template.defaultfilters import slugify, safe


# Create your models here.

class Takim(models.Model):
    ad = models.CharField(max_length=255)
    aciklama = models.TextField()
    uyeler = models.ManyToManyField(to='kullanici.Kullanici', related_name='takimlar', null=True)
    slug = models.SlugField(blank=True)

    class Meta:
        verbose_name = 'Takım'
        verbose_name_plural = 'Takımlar'

    def __str__(self):
        return self.ad

    def get_unique_slug(
            self):  # slug'larımızın düzgün bir şekilde artması için yaptık. Bu sayede sürekli değişecek ve aynı isimde post geldiğinde hata almayacağız
        sayi = 0
        slug = slugify(unidecode(self.ad))
        new_slug = slug
        while Takim.objects.filter(slug=new_slug).exists():
            sayi += 1
            new_slug = "{}-{}".format(slug, sayi)
        slug = new_slug
        return slug

    def save(self, *args, **kwargs):
        if self.id is None:
            self.slug = self.get_unique_slug()
        else:
            takim = Takim.objects.get(slug=self.slug)
            if takim.ad != self.ad:
                self.slug = self.get_unique_slug()
        super(Takim, self).save(*args, **kwargs)
        # daha save fonksiyonu işini bitirmeden biz burda override yaptık. Bu sayede modelin slug alanını set ettik.
