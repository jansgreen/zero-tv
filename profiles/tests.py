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
        self.assertTemplatetUsed(response, 'profile/profile.html')

    def test_view_add_POST_adds_new_expense(self):
        response = self.client.post(self.profiles_url, {
            'id': UserProfile.id,
            'default_phone_number' : UserProfile.default_phone_number,
            'default_country' : UserProfile.default_country,
            'default_postcade' : UserProfile.default_postcade,
            'default_town_or_city' : UserProfile.default_town_or_city,
            'default_street_address' : UserProfile.default_street_address,
            'default_county' : UserProfile.default_county,
            'user_id' : UserProfile.user_id
        })
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.new_user_id, 'Luis')