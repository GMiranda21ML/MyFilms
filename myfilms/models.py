from django.db import models

# Create your models here.

class Filme(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    runtime = models.CharField(max_length=50)
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField() 
    poster = models.URLField()

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Filme"
        verbose_name_plural = "Filmes"
