from django.test import TestCase, Client 
from django.urls import reverse
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.bag_url = reverse('bag')
        self.save_movies_url = reverse('save_movies')
        self.id_movie_url = reverse('id_movie', args=[2316])
        self.updata = reverse('updata', args=[200])

    def test_view_bag_GET(self):
        response = self.client.get(self.bag_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_id_movie_GET(self):
        response = self.client.get(self.id_movie_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'bag/Amovie.html')
    
    def test_save_movies_GET(self):
        response = self.client.get(self.save_movies_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'bag/save_movies.html')


