# Generated by Django 3.0.2 on 2020-02-06 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gorev',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('aciklama', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('baslama_tarihi', models.DateField()),
                ('bitis_tarihi', models.DateField()),
                ('gorev_durum', models.CharField(choices=[('bitti', 'Görev Bitti'), ('devam', 'Görev Devam Ediyor')], default='devam', max_length=5)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Görev',
                'verbose_name_plural': 'Görevler',
            },
        ),
        migrations.CreateModel(
            name='GorevDosya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosya', models.FileField(upload_to='gorevler/dosyalar/')),
                ('ad', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'Görev Dosyası',
                'verbose_name_plural': 'Görev Dosyaları',
            },
        ),
        migrations.CreateModel(
            name='GorevGrubu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
                'verbose_name': 'Görev Grubu',
                'verbose_name_plural': 'Görev Grupları',
            },
        ),
        migrations.CreateModel(
            name='Islem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('islem_sureci', models.CharField(choices=[('bitti', 'İşlem Bitti'), ('devam', 'İşlem Devam Ediyor')], default='devam', max_length=5)),
            ],
            options={
                'verbose_name': 'İşlem',
                'verbose_name_plural': 'İşlemler',
            },
        ),
        migrations.CreateModel(
            name='Not',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=255)),
                ('aciklama', models.TextField()),
                ('olusturulma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('gorev', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notlar', to='gorev.Gorev')),
            ],
            options={
                'verbose_name': 'Not',
                'verbose_name_plural': 'Notlar',
            },
        ),
    ]
