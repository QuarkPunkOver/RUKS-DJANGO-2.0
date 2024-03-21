from datetime import date

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.text import slugify
from django.db.models import Sum
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if Movie.objects.filter(slug=self.slug).exists():
                # Если slug уже существует, добавляем к нему уникальный идентификатор
                self.slug += f"-{self.pk}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Genre(models.Model):
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self, page=1):
        return reverse('genre_catalog', kwargs={'slug': self.slug, 'page': page})

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            if Movie.objects.filter(slug=self.slug).exists():
                # Если slug уже существует, добавляем к нему уникальный идентификатор
                self.slug += f"-{self.pk}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"

class Actor(models.Model): # переделать отдельно под актеры и режисеры
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="actors/", blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
                if Movie.objects.filter(slug=self.slug).exists():
                    # Если slug уже существует, добавляем к нему уникальный идентификатор
                    self.slug += f"-{self.pk}"
            super().save(*args, **kwargs)
    def get_absolute_url(self, page=1):
        return reverse('actor_detail', kwargs={"slug": self.slug, 'page': page})

    class Meta:
        verbose_name = "Актеры"
        verbose_name_plural = "Актеры"
        
class Director(models.Model): # переделать отдельно под актеры и режисеры
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание", blank=True)
    image = models.ImageField("Изображение", upload_to="Directors/", blank=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
                if Movie.objects.filter(slug=self.slug).exists():
                    # Если slug уже существует, добавляем к нему уникальный идентификатор
                    self.slug += f"-{self.pk}"
            super().save(*args, **kwargs)
    def get_absolute_url(self, page=1):
        return reverse('Directors_detail', kwargs={"slug": self.slug, 'page': page})

    class Meta:
        verbose_name = "Режиссеры"
        verbose_name_plural = "Режиссеры"

class Movie(models.Model):
    movie_id = models.PositiveIntegerField(primary_key=True, default=1)
    title = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=3, decimal_places=1,default=0)
    plot = models.TextField(default='')
    poster = models.URLField(blank=True, null=True)
    year = models.PositiveSmallIntegerField(default=2024)
    country = models.CharField(default='international',max_length=30)
    directors = models.ManyToManyField(Director, related_name="film_director")
    actors = models.ManyToManyField(Actor, related_name="film_actor")
    genres = models.ManyToManyField(Genre)
    category = models.ForeignKey(Category, default='film', on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(default='none', max_length=130, unique=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            base_slug = slugify(self.title)
            self.slug = base_slug
            counter = 1
            while Movie.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        elif self.title:
            # Если фильм уже существует, обновляем slug
            base_slug = slugify(self.title)
            if self.slug != base_slug and Movie.objects.filter(slug=base_slug).exists():
                # Если slug уже существует, добавляем суффикс
                counter = 1
                while Movie.objects.filter(slug=f"{base_slug}-{counter}").exists():
                    counter += 1
                self.slug = f"{base_slug}-{counter}"
            else:
                self.slug = base_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("movie_detail", kwargs={"slug": self.slug})
