# Generated by Django 3.0.2 on 2020-01-29 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0002_auto_20200129_0326'),
        ('gorev', '0004_auto_20200129_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gorev',
            name='proje',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gorevler', to='proje.Proje'),
        ),
    ]
