# Generated by Django 3.0.2 on 2020-02-06 23:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gorev', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proje', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='not',
            name='kullanici',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notlar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='islem',
            name='gorev',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='islemler', to='gorev.Gorev'),
        ),
        migrations.AddField(
            model_name='gorevgrubu',
            name='proje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gorev_gruplari', to='proje.Proje'),
        ),
        migrations.AddField(
            model_name='gorevdosya',
            name='gorev',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dosyalar', to='gorev.Gorev'),
        ),
        migrations.AddField(
            model_name='gorevdosya',
            name='yukleyen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gorev_dosyalari', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='gorev',
            name='gorev_grubu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gorevler', to='gorev.GorevGrubu'),
        ),
        migrations.AddField(
            model_name='gorev',
            name='proje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gorevler', to='proje.Proje'),
        ),
        migrations.AddField(
            model_name='gorev',
            name='uyeler',
            field=models.ManyToManyField(null=True, related_name='gorevler', to=settings.AUTH_USER_MODEL),
        ),
    ]
