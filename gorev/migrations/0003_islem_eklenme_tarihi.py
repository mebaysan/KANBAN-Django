# Generated by Django 3.0.2 on 2020-02-06 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gorev', '0002_auto_20200207_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='islem',
            name='eklenme_tarihi',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]