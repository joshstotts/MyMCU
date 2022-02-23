from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('allMovies/', views.allMovies, name='allMovies'),
    path('favorites/', views.favorites_index, name='index'),
    path('favorites/create/', views.FavoriteCreate.as_view(), name='favorites_create'),
    path('favorites/<int:favorite_id>/', views.favorites_detail, name='detail'),
    path('favorites/<int:pk>/update/', views.FavoriteUpdate.as_view(), name='favorites_update'),
    path('favorites/<int:pk>/delete/', views.FavoriteDelete.as_view(), name='favorites_delete'),
    path('favorites/<int:favorite_id>/add_watch', views.add_watch, name='add_watch'),

]