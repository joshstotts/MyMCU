from django.shortcuts import render, redirect
from .models import Favorite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WatchForm

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

def favorites_detail(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    watch_form = WatchForm
    return render(request, 'favorites/detail.html', {
        'favorite': favorite,
        'watch_form': watch_form
    })

def add_watch(request, favorite_id):
    form = WatchForm(request.POST)
    if form.is_valid():
        new_watch = form.save(commit=False)
        new_watch.favorite_id = favorite_id
        new_watch.save()
    return redirect('detail', favorite_id=favorite_id)


class FavoriteCreate(CreateView):
    model = Favorite
    fields = '__all__'

class FavoriteUpdate(UpdateView):
    model = Favorite
    fields = ('rating', 'thoughts')

class FavoriteDelete(DeleteView):
    model = Favorite
    success_url = '/favorites/'

