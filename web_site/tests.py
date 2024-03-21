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