from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return redirect('inicial')

    return render(request, 'index.html')


def buscar(request):
    key = '9882acd4'

    def filme(title):
        url = f'https://www.omdbapi.com/?t={title}&apikey={key}'

        response = requests.get(url)

        if response.status_code == 200:
            movie_data = response.json()

            if movie_data.get('Response') == 'True':
                movie_info = {
                    "Title": movie_data.get('Title'),
                    "Year": movie_data.get('Year'),
                    "Runtime": movie_data.get('Runtime'),
                    "Genre": movie_data.get('Genre'),
                    "Director": movie_data.get('Director'),
                    "Plot": movie_data.get('Plot'),
                    "Poster": movie_data.get('Poster')
                }
                return movie_info
            else:
                return {"Error": movie_data.get('Error')}
        else:
            return {"Error": f"Erro na requisição: {response.status_code}"}

    movie_title = request.GET.get('title')

    if movie_title:
        movie_info = filme(movie_title)
    else:
        movie_info = None

    return render(request, 'buscar.html', {'movie_info': movie_info})

