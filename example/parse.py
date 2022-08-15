from django.core.management.base import BaseCommand
import requests
from django_films.models import  Movie


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'  # noqa: A003, VNE003

    def handle(self, *args, **options):
        head = {
            'X-API-KEY': '538d2c9d-0ff2-449a-a865-613e7f96d144',
            'Content-Type': 'application/json',
        }
        for i in range(300, 310):
            url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{i}'

            response = requests.get(url, headers=head).json()

            nameRu = response['nameRu']
            nameOrigina = response['nameOriginal']
            posterUrl = response['posterUrl']
            poster_get = requests.get(posterUrl)
            poster_name = "".join(nameOrigina.split())
            poster_down = open(f'C:/Users/admin/Documents/django_films/media/movies/{poster_name}.jpg', 'wb')
            poster_down.write(poster_get.content)
            poster_down.close()
            poster_path = 'movies/' + poster_name + '.jpg'
            year = response['year']
            description = response['description']
            slogan = response['slogan']
            countries = response['countries'][0]['country']
            genress = response['genres'][0]['genre']

            try:
                Movie.objects.get(
                    title=nameRu,
                    tagline=slogan,
                    description=description,
                    poster=poster_path,
                    year=year,
                    county=countries,
                    directors=None,
                    actors=None,
                    genres=1,
                    world_premiere=None,
                    budget=None,
                    fees_in_usa=None,
                    fees_in_world=None,
                    # category=Category.objects.get(id=1, name='Films', description='movie', url='movie',
                    #                                         description_en='movie', description_ru='movie',
                    #                                         name_en='Films',
                    #                                         name_ru='Фильмы'),
                    url=None,
                    draft=False
                )
            except Movie.DoesNotExist:
                Movie.objects.create(

                    title=nameRu,
                    tagline=slogan,
                    description=description,
                    poster=poster_path,
                    year=year,
                    county=countries,
                    directors=None,
                    actors=None,
                    genres=1,
                    world_premiere=None,
                    budget=None,
                    fees_in_usa=None,
                    fees_in_world=None,
                    # category=Category.objects.create(name='Films', description='movie', url='movie',
                    #                                         description_en='movie', description_ru='movie',
                    #                                         name_en='Films',
                    #                                         name_ru='Фильмы'),
                    url=None,
                    draft=False
                )
