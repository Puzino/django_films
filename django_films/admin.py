from django.contrib import admin

from .models import Category, Actor, Rating, RatingStats, Genre, Reviews, Movie, MovieShots

admin.site.register(Category)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStats)
admin.site.register(Genre)
admin.site.register(Reviews)
admin.site.register(Movie)
admin.site.register(MovieShots)
