# Generated by Django 3.0.2 on 2020-02-03 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kullanici', '0011_kullanici_gorevler'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kullanici',
            name='gorevler',
        ),
        migrations.RemoveField(
            model_name='kullanici',
            name='takimlar',
        ),
    ]
