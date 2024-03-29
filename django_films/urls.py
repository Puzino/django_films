from django.urls import path

from . import views

urlpatterns = [
    path('', views.MovieViews.as_view(), name='index'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('search/', views.Search.as_view(), name='search'),
    path('json_filter/', views.JsonFilterMoviesView.as_view(), name='json_filter'),
    path('add_rating/', views.AddStarRating.as_view(), name='add_rating'),
    path('<slug:slug>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail'),

]
