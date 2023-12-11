from django.shortcuts import render
import requests
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def movie_recommendation(request):
    base_url = 'https://api.themoviedb.org/3'
    api_key = '63e59cef97d12ab92bb0553eafb80bd9'
    
    query = request.GET.get('query', '')
    
    # Fetch top rated movies by default
    if query:
        endpoint = '/search/movie'
        params = {'api_key': api_key, 'query': query}
    else:
        endpoint = '/movie/top_rated'
        params = {'api_key': api_key}
    
    response = requests.get(f'{base_url}{endpoint}', params=params)
    data = response.json()

    movies = []

    for movie in data.get('results', []):
        movie_details = {
            'id': movie.get('id'),
            'title': movie.get('title'),
            'rating': movie.get('vote_average'),
            'poster_path': f'https://image.tmdb.org/t/p/w500/{movie.get("poster_path")}' if movie.get('poster_path') else None,
        }
        movies.append(movie_details)

    context = {'movies': movies, 'query': query}
    
    return render(request, 'top_rated_movies.html', context)
