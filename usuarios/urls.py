from django.urls import path
from usuarios.views import inicial, login, logout, cadastro

urlpatterns = [
    path('inicial/', inicial, name = 'inicial'),
    path('login/', login, name = 'login'),
    path('cadastro/', cadastro, name = 'cadastro'),
    path('logout/', logout, name = 'logout'),
]
