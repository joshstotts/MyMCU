from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def allMovies(request):
    return render(request, 'allMovies.html')

def favorites(request):
    return render(request, 'favorites/index.html')

