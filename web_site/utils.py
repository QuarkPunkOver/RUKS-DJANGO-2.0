import requests
from .models import Movie

def fetch_movie_data(movie_id):
    url = f"http://127.0.0.1:8000/{movie_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Разбор данных и создание объекта модели
        movie = Movie(
            movie_id=data['movie_id'],
            title=data['title'],
            rating=data['rating'],
            plot='\n'.join(data['plot']),
            poster=data['poster'],
            year=data['year'],
            country=', '.join(data['country']),
            # Продолжайте аналогично для остальных полей модели
        )
        movie.save()
        return movie
    else:
        return None