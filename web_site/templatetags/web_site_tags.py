from django import template
from django.core.exceptions import ObjectDoesNotExist
from web_site.models import Movie
register = template.Library()

@register.simple_tag()
def get_movie_rating(movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
        ratings = movie.rating.all()
        if ratings.exists():
            return sum(rating.avg_rating for rating in ratings) / ratings.count()
        else:
            return 0
    except Movie.DoesNotExist:
        return 0

@register.filter
def correct_num(num: int):
    return f'{num:,.0f}'.replace(',', ' ')