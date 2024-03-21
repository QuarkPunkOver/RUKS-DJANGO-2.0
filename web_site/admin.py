from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Actor, Category, Movie, Genre, Director


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'country', 'rating', 'year', 'slug')
    list_filter = ('category', 'rating', 'year', 'genres', 'country')
    search_fields = ('title', 'category__name')
    readonly_fields = ('get_poster',)
    save_on_top = True
    fields = (
        ('title', 'movie_id'), ('plot'), ('poster', 'get_poster'),
        ('year', 'world_premiere', 'country'),
        ('directors', 'actors', 'genres',),
        ('budget', 'fess_in_world',), ('rating',), ('category'),
        ('slug', 'draft')
    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="50" height="60">')

    get_poster.short_description = 'Постер'

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'age')
    readonly_fields = ('get_image',)
    list_display_links = ('name', 'slug', 'age')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Фото'

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug', 'age')
    readonly_fields = ('get_image',)
    list_display_links = ('name', 'slug', 'age')

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60">')

    get_image.short_description = 'Фото'

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')
    search_fields = ('name',)

