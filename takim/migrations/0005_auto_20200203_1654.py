# Generated by Django 3.0.2 on 2020-02-03 13:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('takim', '0004_auto_20200203_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takim',
            name='uyeler',
            field=models.ManyToManyField(null=True, related_name='takimlar', to=settings.AUTH_USER_MODEL),
        ),
    ]
