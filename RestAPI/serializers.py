from rest_framework import serializers

from web_site.models import Actor, Movie, Genre, Category


class RecursiveSerializer(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class FilterReviewSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class MoviesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'year', 'slug')


class MovieListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    genres = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)
    actors = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)
    directors = serializers.SlugRelatedField(slug_field='slug', read_only=True, many=True)

    class Meta:
        model = Movie
        exclude = ('draft',)


class ActorsListSerializer(serializers.ModelSerializer):
    film_actor = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actor
        fields = ('name', 'pk', 'age', 'film_actor', 'slug')


class ActorListSerializer(serializers.ModelSerializer):
    film_actor = serializers.StringRelatedField(many=True)

    class Meta:
        model = Actor
        fields = '__all__'


class GenresListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'id', 'slug')


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class CategoriesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
