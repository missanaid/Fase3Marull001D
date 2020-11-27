from django.test import TestCase
from anime.models import Galeria


class GaleriaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_galeria = Galeria.objects.create(id='2faf35dd-4f02-4f05-abe8-a9f4b064a201', nombre_anime='Ranma 1/2',
                                              descripcion='Prueba', imagen='https://k62.kn3.net/taringa/C/A/8/B/C/7/CaserasLove/4D8.jpg')

    def setUp(self):
        print("Test Correcto")
        pass

    def test_nombre_anime_label(self):
        galeria = Galeria.objects.get(
            id='2faf35dd-4f02-4f05-abe8-a9f4b064a201')
        field_label = galeria._meta.get_field('nombre_anime').verbose_name
        self.assertEquals(field_label, 'nombre anime')

    def test_descripcion_label(self):
        galeria = Galeria.objects.get(
            id='2faf35dd-4f02-4f05-abe8-a9f4b064a201')
        field_label = galeria._meta.get_field('descripcion').verbose_name
        self.assertEquals(field_label, 'descripcion')

    def test_nombre_anime_max_length(self):
        galeria = Galeria.objects.get(
            id='2faf35dd-4f02-4f05-abe8-a9f4b064a201')
        max_length = galeria._meta.get_field('nombre_anime').max_length
        self.assertEquals(max_length, 200)

    def test_descripcion_max_length(self):
        galeria = Galeria.objects.get(
            id='2faf35dd-4f02-4f05-abe8-a9f4b064a201')
        max_length = galeria._meta.get_field('descripcion').max_length
        self.assertEquals(max_length, 1000)

    def test_get_absolute_url(self):
        galeria = Galeria.objects.get(
            id='2faf35dd-4f02-4f05-abe8-a9f4b064a201')
        self.assertEquals(galeria.get_absolute_url(),
                          '/anime/galeria/2faf35dd-4f02-4f05-abe8-a9f4b064a201')
