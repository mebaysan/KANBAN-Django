from django.contrib import admin
from kullanici.models import Kullanici
from django.contrib.auth.models import Permission



admin.site.register(Kullanici)
admin.site.register(Permission)

admin.site.site_header = "KANBAN Uygulama Paneli"
admin.site.site_title = "KANBAN Admin Portal"
admin.site.index_title = "KANBAN Yönetim Paneline Hoşgeldiniz"