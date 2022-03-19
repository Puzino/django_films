from django import template

from django_films.models import Category, Movie

register = template.Library()


@register.simple_tag()
def get_categories():
    """Вывод всех категорий"""
    return Category.objects.all()


@register.inclusion_tag('django_films/tags/last_movie.html')
def get_last_movies(count=5):
    movies = Movie.objects.filter(draft=False).order_by('id')[:count]
    return {'last_movies': movies}
