from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from anime.models import Galeria
from anime.views import *


class GaleriaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_galery = 2

        with open('anime/static/img/logo.png', 'rb') as file:
            document = SimpleUploadedFile(
                file.name, file.read(), content_type='image/png')

        for galeria_id in range(number_of_galery):
            test_galeria = Galeria.objects.create(
                nombre_anime=f'Rey Leon {galeria_id}',
                descripcion=f'Prueba {galeria_id}',
                imagen=document
            )

            test_galeria.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/anime/galeria/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('galeria'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('galeria'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html', 'galeria.html')
