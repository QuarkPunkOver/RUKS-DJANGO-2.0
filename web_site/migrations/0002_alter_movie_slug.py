# Generated by Django 5.0.3 on 2024-03-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='slug',
            field=models.SlugField(default='n', max_length=130, unique=True),
        ),
    ]
