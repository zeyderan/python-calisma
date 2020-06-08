from django.shortcuts import render
from .models import Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies' : movies
    }
    return render(request,'movies/list.html',context)
# buradaki movie_id ile urls.py deki <int:movie_id> örtüşmelidir.
def detail(request, movie_id):
    return render(request,'movies/detail.html')

def search(request):
    return render(request,'movies/search.html')