# Generated by Django 5.0.3 on 2024-03-09 14:15

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Возраст')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='actors/', verbose_name='Изображение')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Актеры и режиссеры',
                'verbose_name_plural': 'Актеры и режиссеры',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('slug', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('slug', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('movie_id', models.PositiveIntegerField(default=1, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
                ('plot', models.TextField(default='')),
                ('poster', models.URLField(blank=True, null=True)),
                ('year', models.PositiveSmallIntegerField(default=2024)),
                ('country', models.CharField(default='international', max_length=30)),
                ('world_premiere', models.DateField(default=datetime.date.today)),
                ('budget', models.PositiveIntegerField(blank=True, default=0)),
                ('fess_in_world', models.PositiveIntegerField(blank=True, default=0)),
                ('slug', models.SlugField(default='none', max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(related_name='film_actor', to='web_site.actor')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='web_site.category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='web_site.actor')),
                ('genres', models.ManyToManyField(to='web_site.genre')),
            ],
        ),
    ]
