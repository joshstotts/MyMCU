from django.shortcuts import render
from .models import Favorite
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def allMovies(request):
    return render(request, 'allMovies.html')

def favorites_index(request):
    favorites = Favorite.objects.all()
    return render(request, 'favorites/index.html', {'favorites': favorites})



class FavoriteCreate(CreateView):
    model = Favorite
    fields = '__all__'



