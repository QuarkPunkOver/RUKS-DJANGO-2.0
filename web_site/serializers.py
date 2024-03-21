from imdb import Cinemagoer

from rest_framework import serializers
from .models import Movie, Actor, Director, Genre

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title', 'rating', 'plot', 
                  'poster', 'year', 'country', 'directors', 
                  'actors', 'genres', 'world_premiere', 'budget',
                    'fess_in_world', 'category', 'slug', 'draft']

class MovieInfoSerializer(serializers.Serializer):
    def get_movie_info(self, movie_id):
        ia = Cinemagoer()
        # Получаем информацию о фильме по его IMDb ID
        movie = ia.get_movie(movie_id)
        # Извлекаем нужные данные о фильме
        imdb_id = movie_id
        title = movie['title']
        rating = movie.get('rating')
        plot = movie.get('plot')
        cover_url = movie.get('full-size cover url')
        year = movie.get('year')
        country = movie.get('country')
        genres = movie.get('genres')
        
        def get_movie_actors_ids(movie_id):
            actors = movie.get('cast')
            actor_ids = [actor.getID() for actor in actors]  # Получаем идентификаторы актеров
            return actor_ids

        def get_movie_directors_ids(movie_id):
            directors = movie.get('directors')
            director_ids = [director.getID() for director in directors]  # Получаем идентификаторы режиссеров
            return director_ids     
        actors_ids = get_movie_actors_ids(movie_id)
        directors_ids = get_movie_directors_ids(movie_id)
        
        
        return {
            "movie_id" : imdb_id,
            "title": title,
            "rating": rating,
            "plot": plot,
            "poster" : cover_url,
            "year" : year,
            "country" : country,
            "directors" : directors_ids,
            "actors" : actors_ids,
            "genres" : genres,
        }
    
    @staticmethod
    def get_person_info(person_id):
        ia = Cinemagoer()
        person = ia.get_person(person_id)
        name = person.get('name')
        photo = person.get('full-size headshot')
        return name, photo

    def add_movie_to_db(self, movie_data):
        movie_info = self.get_movie_info(movie_data['movie_id'])
        
        movie = Movie.objects.create(
            title=movie_data['title'][2:-2],
            rating=movie_data['rating'][2:-2],
            plot=movie_data['plot'][2:-2],
            poster=movie_data['poster'][2:-2],
            year=movie_data['year'][2:-2],
            country=movie_data['country'][2:-2]
        )
        # Обрабатываем жанры
        for genre_name in movie_data['genres']:
            genre, _ = Genre.objects.get_or_create(name=genre_name)
            movie.genres.add(genre)

            # Обрабатываем режиссеров
        for director_id in movie_data['directors']:
            director_name, director_photo = self.get_person_info(director_id)
            director, _ = Director.objects.get_or_create(name=director_name)
            if director_photo:
                director.image = director_photo
                director.save()
            movie.directors.add(director)

        # Обрабатываем актеров
        for actor_id in movie_data['actors']:
            actor_name, actor_photo = self.get_person_info(actor_id)
            actor, _ = Actor.objects.get_or_create(name=actor_name)
            if actor_photo:
                actor.image = actor_photo
                actor.save()
            movie.actors.add(actor)