from django.test import TestCase, Client 
from django.urls import reverse
from .models import Movies, Genders
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.bag_url = reverse('bag')
        self.save_movies_url = reverse('save_movies')
        self.id_movie_url = reverse('id_movie', args=['2316'])
        self.add_movie = reverse('add_Movies')
        self.new_genders = Genders.objects.create(
            name='Test_genders',
            pk = 222
        )

    def test_view_add_POST_adds_new_expense(self):
        response = self.client.post(self.add_movie, {
            'popularity' : 000,
            'vote' : 000,
            'video' : 'False',
            'poster' : 'https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/12274683_707766029358497_3476638484944935560_n.jpg',
            'adult' : 'False',
            'backdrop' : 'https://scontent-lga3-1.xx.fbcdn.net/v/t1.0-9/12274683_707766029358497_3476638484944935560_n.jpg',
            'Language' : 'UnK',
            'original_title': 'Jansgreen',
            'genres_ids' : [12, 14],
            'title' : 'jansgreen',
            'vote_average' : 111,
            'overview' : 'Test jansgreen movie',
            'release_date' : '2020-02-02',
            'price' : 1000000.00,
        })
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.new_genders.name, 'Test_genders')
    
    def test_view_add_POST_adds_new_expense(self):
        response = self.client.post(self.add_movie)
        self.assertEquals(response.status_code, 302)
    

    def test_id_movie_GET(self):
        response = self.client.get(self.id_movie_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'bag/Amovie.html')
    
    def test_save_movies_GET(self):
        response = self.client.get(self.save_movies_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'bag/save_movies.html')