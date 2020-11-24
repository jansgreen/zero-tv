from django.test import TestCase
from .models import Genders

class testGenders(TestCase):
    fixtures = ["Genders.json"]

    def test_should_create_group(self):
        movie = Genders.objects.get(pk=12)
        self.assertEqual(movie.name, movie.name)