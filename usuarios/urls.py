from django.urls import path
from usuarios.views import inicial, login, logout

urlpatterns = [
    path('inicial/', inicial, name = 'inicial'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout')
]
