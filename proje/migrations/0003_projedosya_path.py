# Generated by Django 3.0.2 on 2020-02-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0002_projedosya_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='projedosya',
            name='path',
            field=models.FilePathField(blank=True, null=True),
        ),
    ]
