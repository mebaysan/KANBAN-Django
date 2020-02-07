from django import template
from proje.models import Proje
from gorev.models import Gorev

register = template.Library()


@register.filter(name='proje_kac_gorev_var')
def proje_kac_gorev_var(proje):
    toplam_gorev = proje.gorevler.all().count()
    biten_gorev = proje.gorevler.filter(gorev_durum='bitti').count()

    return "{}/{}".format(biten_gorev, toplam_gorev)


@register.filter(name='gorev_kac_islem_var')
def gorev_kac_islem_var(gorev):
    toplam_islem = gorev.islemler.all().count()
    biten_islemler = gorev.islemler.filter(islem_sureci='bitti').count()
    return "{}/{}".format(biten_islemler, toplam_islem)
