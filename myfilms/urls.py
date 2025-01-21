from django.urls import path
from myfilms.views import index, buscar
urlpatterns = [
    path('', index, name = 'index'),
    path('buscar/', buscar, name = 'buscar')
]
