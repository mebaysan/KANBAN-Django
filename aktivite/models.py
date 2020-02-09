from django.db import models


class Aktivite(models.Model):  # Aktivite geçmişi oluşturmak için kullanacağımız model
    aktivite_tipleri = (
        ('silme', 'Silindi'),
        ('guncelleme', 'Güncellendi'),
        ('olusturma', 'Oluşturuldu'),
        ('ekleme','Eklendi')
    )
    proje = models.ForeignKey(to='proje.Proje', on_delete=models.CASCADE, related_name='aktiviteler')
    gorev = models.ForeignKey(to='gorev.Gorev', on_delete=models.CASCADE, related_name='aktiviteler', null=True,
                              blank=True)
    kullanici = models.ForeignKey(to='kullanici.Kullanici', on_delete=models.CASCADE, related_name='aktiviteler')
    aktivite_tipi = models.CharField(choices=aktivite_tipleri, max_length=20)
    aktivite = models.TextField()
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Aktiviteler'
        verbose_name = 'Aktivite'
    def __str__(self):
        return self.aktivite