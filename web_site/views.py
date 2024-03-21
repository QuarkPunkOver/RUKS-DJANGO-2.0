import json

from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import MultipleObjectMixin

from web_site.forms import UserRegisterForm, UserLoginForm
from web_site.models import Movie, Genre, Actor

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MovieInfoSerializer
from .serializers import MovieSerializer
from django.http import Http404
from .models import Movie, Actor, Genre, Director
from .utils import fetch_movie_data
from django.utils.text import slugify
import json
from imdb import Cinemagoer
from django.http import JsonResponse

class MovieInfoView(APIView):
    @staticmethod
    def get_person_info(person_id):
        ia = Cinemagoer()
        person = ia.get_person(person_id)
        name = person.get('name')
        photo = person.get('full-size headshot')
        return name, photo

    def get(self, request, movie_id):
        if 'write_data' in request.path:
            serializer = MovieInfoSerializer(data={'movie_id': movie_id})
            
            if serializer.is_valid():
                movie_info = serializer.get_movie_info(movie_id)
                movie_data = serializer.get_movie_info(movie_id)
                
                # Проверка наличия фильма в базе данных
                existing_movie = Movie.objects.filter(movie_id=movie_data['movie_id']).first()
                if existing_movie:
                    return Response({'message': 'Фильм уже существует'}, status=status.HTTP_400_BAD_REQUEST)
                
                # Создание объекта модели фильма и сохранение его в базе данных
                movie = Movie(
                    movie_id=movie_data['movie_id'],
                    title=movie_data['title'],
                    rating=movie_data['rating'],
                    plot=movie_data['plot'],
                    poster=movie_data['poster'],
                    year=movie_data['year'],
                    country=movie_data['country'],
                    # Добавьте обработку остальных полей...
                )
                movie.save()

                # Обработка жанров
                for genre in movie_data['genres']:
                    movie_genre, created = Genre.objects.get_or_create(name=genre)
                    movie.genres.add(movie_genre)

                # Обработка режиссеров
                for director_id in movie_data['directors']:
                    director_name, director_photo = self.get_person_info(director_id)
                    director, _ = Director.objects.get_or_create(name=director_name)
                    if director_photo:
                        director.image = director_photo
                        director.save()
                    movie.directors.add(director)
                            
                # Обработка актеров
                for actor_id in movie_data['actors']:
                    actor_name, actor_photo = self.get_person_info(actor_id)
                    actor, _ = Actor.objects.get_or_create(name=actor_name)
                    if actor_photo:
                        actor.image = actor_photo
                        actor.save()
                    movie.actors.add(actor)

                return Response(movie_data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = MovieInfoSerializer(data={'movie_id': movie_id})
            
            if serializer.is_valid():
                movie_info = serializer.get_movie_info(movie_id)
                movie_data = serializer.get_movie_info(movie_id)
                
                # Создание объекта модели фильма и сохранение его в базе данных
                movie = Movie(
                    movie_id=movie_data['movie_id'],
                    title=movie_data['title'],
                    rating=movie_data['rating'],
                    plot=movie_data['plot'],
                    poster=movie_data['poster'],
                    year=movie_data['year'],
                    country=movie_data['country'],
                    # Добавьте обработку остальных полей...
                )
                
                # Обработка жанров
                for genre in movie_data['genres']:
                    movie_genre, created = Genre.objects.get_or_create(name=genre)

                return Response(movie_data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class MoviesFilter:

    def get_genres(self):
        return Genre.objects.all().order_by('name')

    def get_years(self):
        return Movie.objects.values_list('year', flat=True).distinct().order_by('-year')

    def get_countries(self):
        return Movie.objects.values_list('country', flat=True).distinct().order_by('country')


class MoviesView(MoviesFilter, View):
    model = Movie
    template_name = 'web_site/index.html'

    def get(self, request):
        carousel_movies = Movie.objects.order_by('rating')[:12].prefetch_related('genres')
        premieres = Movie.objects.order_by().prefetch_related('genres').select_related('category')[:8]
        new_movies = Movie.objects.order_by('-year')[:18].prefetch_related('genres')
        try:
            cartoon_id = Genre.objects.get(slug='multfilm')
        except Genre.DoesNotExist:
            cartoon_id = None
        cartoons_list = Movie.objects.filter(genres=cartoon_id).order_by('-year')[:12].prefetch_related('genres')

        context = {'carousel_list': carousel_movies, 'premieres_list': premieres, 'cartoons_list': cartoons_list,
                   'new_movies_list': new_movies}
        return render(request, 'web_site/index.html', context)


class SingleMovieView(MoviesFilter, DetailView):
    model = Movie
    template_name = 'web_site/movie_detail.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_films'] = Movie.objects.filter(
            genres__in=(kwargs['object'].genres.all().values_list('pk').distinct()))[:6]
        return context
    
class SinglePlayerView(MoviesFilter, DetailView):
    model = Movie
    template_name = 'web_site/videoplayerblank.html'
    context_object_name = 'movie'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recommended_films'] = Movie.objects.filter(
            genres__in=(kwargs['object'].genres.all().values_list('pk').distinct()))[:6]
        return context
    
class ActorDetailView(DetailView, MultipleObjectMixin):
    model = Actor
    template_name = 'web_site/actor_detail.html'
    context_object_name = 'actor'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        object_list = Movie.objects.filter(actors=self.object).prefetch_related('genres')
        context = super().get_context_data(object_list=object_list, **kwargs)

        return context


class DirectorDetailView(DetailView, MultipleObjectMixin):
    model = Director
    template_name = 'web_site/directors_detail.html'
    context_object_name = 'director'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        object_list = Movie.objects.filter(directors=self.object).prefetch_related('genres')
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class CatalogView(MoviesFilter, ListView):
    model = Movie
    template_name = 'web_site/catalog_movies.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_queryset(self):
        if self.kwargs.get('slug'):
            genres = Genre.objects.get(slug=self.kwargs['slug'])
            queryset = Movie.objects.filter(genres=genres.id).prefetch_related('genres')
        else:
            queryset = Movie.objects.order_by('year').prefetch_related('genres')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('slug'):
            context['current_genre'] = self.kwargs['slug']
        return context


class FilterMoviesView(MoviesFilter, ListView):
    template_name = 'web_site/catalog_movies.html'
    paginate_by = 12
    context_object_name = 'movies'

    def result_queryset(self, genres, year, country):
        if year and genres and country:
            queryset = Movie.objects.filter(genres=genres, year=year, country=country).prefetch_related('genres')
        elif year is None and (genres and country):
            queryset = Movie.objects.filter(genres=genres, country=country).distinct().prefetch_related('genres')
        elif genres is None and (year and country):
            queryset = Movie.objects.filter(year=year, country=country).distinct().prefetch_related('genres')
        elif country is None and (year and genres):
            queryset = Movie.objects.filter(year=year, genres=genres).distinct().prefetch_related('genres')
        else:
            queryset = Movie.objects.filter(
                Q(genres=genres) | Q(country=country) | Q(year=year)).distinct().prefetch_related('genres')

        return queryset

    def get_queryset(self):
        genres = None
        if self.request.GET.get('genre') not in ['Genre', 'Жанр']:
            genres = Genre.objects.get(name=self.request.GET.get('genre')).id

        country = None if self.request.GET.get('country') in ['Country', 'Страна'] else self.request.GET.get('country')
        year = None if self.request.GET.get('year') in ['Year', 'Год'] else self.request.GET.get('year')
        queryset = self.result_queryset(genres, year, country).order_by('year')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["url_genre"] = f'genre={self.request.GET.get("genre")}&'
        context["country"] = f"year={self.request.GET.get('year')}&"
        context["year"] = f"country={self.request.GET.get('country')}&"
        return context



class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'web_site/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'web_site/login.html'
    next_page = 'home'


def logout_user(request):
    logout(request)
    return redirect('login')


def handle_not_found(request, exception):
    return render(request, '404.html')


class Search(ListView):
    template_name = 'web_site/catalog_movies.html'
    context_object_name = 'movies'
    paginate_by = 12

    def get_queryset(self):
        return Movie.objects.filter(title__icontains=self.request.GET.get('q').title())

    def get_context_data(self, *args, **kwargs):
        context = super(Search, self).get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def about_us(request):
    return render(request, 'web_site/about.html')


def faq_page(request):
    return render(request, 'web_site/help_page.html')

def terms_page(request):
    return render(request, 'web_site/terms_of_use.html')



        