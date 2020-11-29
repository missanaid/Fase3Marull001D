from django.test import TestCase
from anime.models import Galeria, Anime


class GaleriaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_galeria = Galeria.objects.create(id='7f595706-0248-4026-9c18-dc3f9a16ca1a', nombre_anime='Ranma 1/2',
                                              descripcion='Prueba', imagen='https://k62.kn3.net/taringa/C/A/8/B/C/7/CaserasLove/4D8.jpg')

    def setUp(self):
        print("Test Correcto")
        pass

    def test_nombre_anime_label(self):
        galeria = Galeria.objects.get(
            id='7f595706-0248-4026-9c18-dc3f9a16ca1a')
        field_label = galeria._meta.get_field('nombre_anime').verbose_name
        self.assertEquals(field_label, 'nombre anime')

    def test_descripcion_label(self):
        galeria = Galeria.objects.get(
            id='7f595706-0248-4026-9c18-dc3f9a16ca1a')
        field_label = galeria._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')

    def test_nombre_anime_max_length(self):
        galeria = Galeria.objects.get(
            id='7f595706-0248-4026-9c18-dc3f9a16ca1a')
        max_length = galeria._meta.get_field('nombre_anime').max_length
        self.assertEquals(max_length, 200)

    def test_descripcion_max_length(self):
        galeria = Galeria.objects.get(
            id='7f595706-0248-4026-9c18-dc3f9a16ca1a')
        max_length = galeria._meta.get_field('descripcion').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        galeria = Galeria.objects.get(
            id='7f595706-0248-4026-9c18-dc3f9a16ca1a')
        self.assertEquals(galeria.get_absolute_url(),
                          '/galeria/7f595706-0248-4026-9c18-dc3f9a16ca1a')


class AnimeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_anime = Anime.objects.create(id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd', nombre_anime='Boku no Hero',
                                          episodios=125, imagen='https://images-na.ssl-images-amazon.com/images/I/91kjVOEopVL._AC_SL1500_.jpg')

    def setUp(self):
        print("Test Correcto")
        pass

    def test_nombre_anime_label(self):
        anime = Anime.objects.get(
            id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
        field_label = anime._meta.get_field('nombre_anime').verbose_name
        self.assertEquals(field_label, 'nombre anime')

    def test_descripcion_label(self):
        anime = Anime.objects.get(
            id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
        field_label = anime._meta.get_field('episodios').verbose_name
        self.assertEquals(field_label, 'episodios')

    def test_nombre_anime_max_length(self):
        anime = Anime.objects.get(
            id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
        max_length = anime._meta.get_field('nombre_anime').max_length
        self.assertEquals(max_length, 200)

    def test_descripcion_max_length(self):
        anime = Anime.objects.get(
            id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
        max_length = anime._meta.get_field('sinopsis').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        anime = Anime.objects.get(
            id='2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
        self.assertEquals(anime.get_absolute_url(),
                          '/anime/2f5a13fc-1d2b-4b8c-9d4d-3bf6646063bd')
