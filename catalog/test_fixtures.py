from django.test import TestCase
from .models import Genders, Classification, Movies

class testGenders(TestCase):
    fixtures = ["Genders.json"]

    def test_should_create_group(self):
        movie = Genders.objects.get(pk=12)
        self.assertEqual(movie.name, movie.name)

class testClassification(TestCase):
    fixtures = ["Classification.json"]

    def test_should_create_group_Classification(self):
        sorting = Classification.objects.get(pk=1)
        self.assertEqual(sorting.minimum_age, sorting.minimum_age)