from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib import auth
from django.contrib.auth.models import User

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


def cadastro(request):
    form = CadastroForms()

    if request.method == "POST":
        form = CadastroForms(request.POST)
        
        if form.is_valid():
            
            nome = form["nomeCadastro"].value()
            email = form["email"].value()
            senha = form["senha"].value()

            if User.objects.filter(username=nome).exists():
                # messages.error(request, "Este usuário ja existe")
                return redirect("cadastro")
            
            usuario = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )

            usuario.save()
            # messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect("login")
            
    return render(request, "cadastro.html", {"form":form})

def logout(request):
    auth.logout(request)
    return redirect('inicial')