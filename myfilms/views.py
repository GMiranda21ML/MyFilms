from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Filme
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
                return {
                    "Title": movie_data.get('Title'),
                    "Year": movie_data.get('Year'),
                    "Runtime": movie_data.get('Runtime'),
                    "Genre": movie_data.get('Genre'),
                    "Director": movie_data.get('Director'),
                    "Plot": movie_data.get('Plot'),
                    "Poster": movie_data.get('Poster')
                }
        return None

    movie_title = request.GET.get('title')
    movie_info = filme(movie_title) if movie_title else None

    return render(request, 'buscar.html', {'movie_info': movie_info})

@csrf_exempt
def adicionar_filme(request):
    if request.method == "POST":
        title = request.POST.get("title")
        year = request.POST.get("year")
        runtime = request.POST.get("runtime")
        genre = request.POST.get("genre")
        director = request.POST.get("director")
        plot = request.POST.get("plot")
        poster = request.POST.get("poster")

        filme = Filme(
            title=title,
            year=year,
            runtime=runtime,
            genre=genre,
            director=director,
            plot=plot,
            poster=poster
        )
        filme.save()
        messages.success(request, "Filme adicionado com sucesso!")
        return redirect("buscar")
    
    return redirect("index")


def listar_filmes(request):
    filmes = Filme.objects.all() 
    return render(request, 'minhaLista.html', {'filmes': filmes})


def filme_detalhes(request, filme_id):
    filme = get_object_or_404(Filme, pk=filme_id)

    if request.method == "POST":
        filme.delete()
        return redirect('minhaLista')

    return render(request, 'filmeDetalhe.html', {'filme': filme})
