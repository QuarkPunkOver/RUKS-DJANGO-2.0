from django.test import TestCase
from imdb import Cinemagoer
# Create your tests here.
ia = Cinemagoer()
        # Получаем информацию о фильме по его IMDb ID
movie_id = '0075314'
movie = ia.get_movie(movie_id)

yt_search_term = movie.get('year')
print(yt_search_term)
#actorgett = ia.get_person('0000134')

#actors = movie.get('cast')
#actor_ids = [actor.getID() for actor in actors]
#print(actorgett['full-size headshot'])
#print(movie['genre'])
#print(movie['video clips'])
#print(movie.getAsXML('Trailer'))
#print(movie['release info'])
'''
actors = movie.get('cast')
directors = movie.get('directors')
actors_and_directors = {
    "actors": [],
    "directors": []
}

for actor in actors:
        actor_id = actor.get('id')
        actor_name = actor.get('name')
        actor_photo = actor.get('full-size headshot')
        actors_and_directors["actors"].append({
            "id": actor_id,
            "name": actor_name,
            "photo": actor_photo
        })
                
print(actors_and_directors)'''

['airing', 'akas', 'alternate versions', 'awards', 'connections', 'crazy credits', 'critic reviews', 'episodes', 'external reviews', 'external sites',
  'faqs', 'full credits', 'goofs', 'keywords', 'list', 'locations', 'main', 'misc sites', 'news', 'official sites', 'parents guide', 'photo sites',
    'plot', 'quotes', 'recommendations', 'release dates', 'release info', 'reviews', 'sound clips', 'soundtrack', 'synopsis', 'taglines', 'technical',
      'trivia', 'tv schedule', 'video clips', 'vote details']


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
            
serial:
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