from django import template
from proje.models import Proje

register = template.Library()

@register.filter(name='proje_kac_gorev_var')
def proje_kac_gorev_var(proje):
    toplam_gorev = proje.gorevler.all().count()
    biten_gorev = proje.gorevler.filter(gorev_durum='bitti').count()

    return "{}/{}".format(biten_gorev, toplam_gorev)
