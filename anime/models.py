from django.db import models
from django.urls import reverse
import uuid


class Galeria(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,  editable=False)
    nombre_anime = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=1000)
    imagen = models.ImageField(
        upload_to='galeria/', null=True, blank=True)

    class Meta:
        ordering = ['nombre_anime']

    def __str__(self):
        return self.nombre_anime

    def get_absolute_url(self):
        """Devuelve la url para acceder a un registro detallado de el Anime."""
        return reverse('galeria-detail', args=[str(self.id)])


class Anime(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4,  editable=False)
    nombre_anime = models.CharField(max_length=100)
    episodios = models.IntegerField(default=0)
    sinopsis = models.TextField()
    imagen = models.ImageField(
        upload_to='anime/', null=True, blank=True)
    opening = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['nombre_anime']

    def __str__(self):
        """String for representing the Model object."""
        return self.nombre_anime

    def get_absolute_url(self):
        return reverse('anime-detail', args=[str(self.id)])
