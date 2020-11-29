from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from anime.models import Galeria, Anime


class GaleriaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_galery = 2

        with open('anime/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(
                file.name, file.read(), content_type='image/png')

        for galeria_id in range(number_of_galery):
            test_galeria = Galeria.objects.create(
                nombre_anime=f'Naruto{galeria_id}',
                descripcion=f'Prueba {galeria_id}',
                imagen=document
            )

            test_galeria.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/galeria/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('galeria'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('galeria'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'galeria.html')


class AnimeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_anime = 2

        with open('anime/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(
                file.name, file.read(), content_type='image/png')

        for anime_id in range(number_of_anime):
            test_anime = Galeria.objects.create(
                nombre_anime=f'One Piece {anime_id}',
                descripcion=f'Prueba {anime_id}',
                imagen=document
            )

            test_anime.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('anime'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('anime'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'anime.html')
