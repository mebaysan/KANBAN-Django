# Generated by Django 3.0.2 on 2020-02-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aktivite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aktivite',
            name='aktivite_tipi',
            field=models.CharField(choices=[('silme', 'Silme'), ('guncelleme', 'Güncelleme'), ('olusturma', 'Oluşturuldu')], max_length=20),
        ),
    ]