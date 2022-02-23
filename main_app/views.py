from django.shortcuts import render, redirect
from .models import Favorite
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import WatchForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def allMovies(request):
    return render(request, 'allMovies.html')

@login_required
def favorites_index(request):
    favorites = Favorite.objects.filter(user=request.user)
    return render(request, 'favorites/index.html', {'favorites': favorites})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'invalid - try again'
    form = UserCreationForm()
    context = {'form': form, 'error': error_message }
    return render(request, 'registration/signup.html', context)

@login_required
def favorites_detail(request, favorite_id):
    favorite = Favorite.objects.get(id=favorite_id)
    if favorite.user_id != request.user.id:
        return redirect('allMovies')
    watch_form = WatchForm
    return render(request, 'favorites/detail.html', {
        'favorite': favorite,
        'watch_form': watch_form
    })

@login_required
def add_watch(request, favorite_id):
    form = WatchForm(request.POST)
    if form.is_valid():
        new_watch = form.save(commit=False)
        new_watch.favorite_id = favorite_id
        new_watch.save()
    return redirect('detail', favorite_id=favorite_id)


class FavoriteCreate(LoginRequiredMixin, CreateView):
    model = Favorite
    fields = ('title', 'rating', 'thoughts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class FavoriteUpdate(LoginRequiredMixin, UpdateView):
    model = Favorite
    fields = ('rating', 'thoughts')

class FavoriteDelete(LoginRequiredMixin, DeleteView):
    model = Favorite
    success_url = '/favorites/'

