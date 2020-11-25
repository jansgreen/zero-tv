from django.test import TestCase, Client 
from django.urls import reverse
from .models import UserProfile
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.profiles_url = reverse('profiles')
    
    def test_save_movies_GET(self):
        response = self.client.get(self.profiles_url)

        self.assertEquals(response.status_code, 302)
        self.assertTemplateNotUsed(response, 'profile.html')
