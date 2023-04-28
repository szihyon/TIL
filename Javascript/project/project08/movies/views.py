from django.shortcuts import render
from django.views.decorators.http import require_safe
from .models import Movie

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {'movie': movie}
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request):
    top_movies = Movie.objects.order_by('-vote_average')[:10]
    return render(request, 'movies/recommended.html', {'top_movies': top_movies})

