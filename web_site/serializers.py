from imdb import Cinemagoer

from requests import Response
from rest_framework import serializers
from .models import Movie, Actor, Director, Genre
from rest_framework import status

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_id', 'title', 'rating', 'plot', 
                  'poster', 'year', 'country', 'directors', 
                  'actors', 'genres', 'category', 'slug']

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
            if actor_counter.is_limit_reached():
                return Response(status=status.HTTP_200_OK)
            else:
                ia = Cinemagoer()
                person = ia.get_person(person_id)
                name = person.get('name')
                photo = person.get('full-size headshot')
                if photo is None:
                    # Заглушка для URL фотографии
                    placeholder_photo_url = 'https://clipart-library.com/image_gallery/515127.jpg'
                    return name, placeholder_photo_url
                    
                actor_counter.increment()

                return name, photo,
    
                

    def add_movie_to_db(self, movie_data):
        plot = ' '.join(movie_data['plot']) if isinstance(movie_data['plot'], list) else movie_data['plot']
        movie = Movie.objects.create(
            movie_id=movie_data['movie_id'],
            title=movie_data['title'],
            rating=movie_data['rating'],
            plot=plot,
            poster=movie_data['poster'],
            year=movie_data['year'],
            country=movie_data['country'][0]
        )
        
        for genre in movie_data['genres']:
            movie_genre, created = Genre.objects.get_or_create(name=genre)
            movie.genres.add(movie_genre)

        for director_id in movie_data['directors']:
            director_name, director_photo = self.get_person_info(director_id)
            director, _ = Director.objects.get_or_create(name=director_name)
            if director_photo:
                director.image = director_photo
                director.save()
            movie.directors.add(director)
                    
        for actor_id in movie_data['actors']:
            actor_name, actor_photo = self.get_person_info(actor_id)
            actor, _ = Actor.objects.get_or_create(name=actor_name)
            if actor_photo:
                actor.image = actor_photo
                actor.save()
            movie.actors.add(actor)

            
class ActorCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def is_limit_reached(self):
        return self.count >= 15
    
actor_counter = ActorCounter()