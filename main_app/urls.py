from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allMovies/', views.allMovies, name='allMovies'),
    path('favorites/', views.favorites_index, name='index'),
    path('favorites/create/', views.FavoriteCreate.as_view(), name='favorites_create'),
    
]