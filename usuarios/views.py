from django.shortcuts import render, redirect
from usuarios.forms import LoginForms
from django.contrib import auth

# Create your views here.

def inicial(request):
    return render(request, 'inicial.html')


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nomeLogin"].value()
            senha = form["senha"].value()

        usuario = auth.authenticate(
            request,
            username = nome,
            password = senha
        )

        if usuario is not None:
            auth.login(request, usuario)
            # messages.success(request, f"Usuário ({nome}) logado com sucesso")
            return redirect("index")
        else:
            # messages.error(request, "Erro ao efetuar login")
            return redirect("login")

    return render(request, 'login.html', {'form':form})


def logout(request):
    auth.logout(request)
    return redirect('inicial')