# Generated by Django 3.0.2 on 2020-02-03 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorev', '0012_gorev_gorev_durum'),
    ]

    operations = [
        migrations.AddField(
            model_name='gorev',
            name='slug',
            field=models.SlugField(default='as-as'),
            preserve_default=False,
        ),
    ]
