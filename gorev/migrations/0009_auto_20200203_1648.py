# Generated by Django 3.0.2 on 2020-02-03 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gorev', '0008_auto_20200203_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gorev',
            name='sahip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gorevler', to=settings.AUTH_USER_MODEL),
        ),
    ]
