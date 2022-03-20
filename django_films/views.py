from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Movie, Category, Actor


class MovieViews(ListView):
    """Список фильмов"""

    model = Movie
    queryset = Movie.objects.filter(draft=False)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = 'url'


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(DetailView):
    """Вывод страницы акторов и режисёров"""
    model = Actor
    template_name = 'django_films/actor.html'
    slug_field = 'name'
