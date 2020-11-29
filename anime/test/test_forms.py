from django.test import TestCase
from anime.forms import GaleriaForm, AnimeForm
from anime.models import Galeria, Anime
from django.core.files.uploadedfile import SimpleUploadedFile


class GaleriaFormsTest(TestCase):
    def test_valid_form(self):
        def test_valid_form(self):
            a = Galeria.objects.create(
                nombre_anime='Prueba1', descripcion='Prueba')
            data = {'nombre_anime': a.nombre_anime,
                    'descripcion': a.descripcion, }
            form = GaleriaForm(data=data)
            self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Galeria.objects.create(nombre_anime='', descripcion='Prueba')
        data = {'nombre_anime': a.nombre_anime, 'descripcion': a.descripcion, }
        form = GaleriaForm(data=data)
        self.assertFalse(form.is_valid())


class AnimeFormsTest(TestCase):
    def test_valid_form(self):
        def test_valid_form(self):
            a = Anime.objects.create(
                nombre_anime='Prueba1', sinopsis='Prueba')
            data = {'nombre_anime': a.nombre_anime,
                    'sinopsis': a.sinopsis, }
            form = AnimeForm(data=data)
            self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        a = Anime.objects.create(nombre_anime='', sinopsis='Prueba')
        data = {'nombre_anime': a.nombre_anime, 'sinopsis': a.sinopsis, }
        form = AnimeForm(data=data)
        self.assertFalse(form.is_valid())
