from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from takim.models import Takim


class Kullanici(AbstractUser):
    profil_foto = models.ImageField(upload_to='profil/foto/', default='defaults/default.png')
    lokasyon = models.CharField(max_length=255, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='izinler', null=True,
                                              blank=True)  # zorunlu tanımlamamız gerek
    groups = models.ManyToManyField(Group, related_name='gruplar', null=True, blank=True)  # zorunlu tanımlamamız gerek
    password_reset_hash = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Kullanıcı'
        verbose_name_plural = 'Kullanıcılar'
