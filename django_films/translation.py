from modeltranslation.translator import register, TranslationOptions
from .models import Category, Actor, Movie, Genre, MovieShots


@register(Category)
class CategoryTranslationsOption(TranslationOptions):
    fields = ('name', 'description')


@register(Actor)
class ActorTranslationsOption(TranslationOptions):
    fields = ('name', 'description')


@register(Genre)
class GenreTranslationsOption(TranslationOptions):
    fields = ('name', 'description')


@register(Movie)
class MovieTranslationsOption(TranslationOptions):
    fields = ('title', 'tagline', 'description', 'county')


@register(MovieShots)
class MovieShotsTranslationsOption(TranslationOptions):
    fields = ('title', 'description')
