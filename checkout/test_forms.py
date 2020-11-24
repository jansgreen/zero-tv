from django.test import TestCase
from .forms import OrderForm


class TestItemForm(TestCase):
    """
    Testing checkout forms fields
    """

    def test_form_valid_data(self):
        form = OrderForm({
            'full_name': '',
            'email': '',
            'phone_number': '',
            'street_address': '',
            'town_or_city': '',
            'postcade': '',
            'country': '',
            'county': '',

        })
        self.assertFalse(form.is_valid())
        for fields in OrderForm():
            self.assertIn(fields.name, form.errors.keys())
            self.assertEquals(form.errors[fields.name][0], 'This field is required.')
    
    def test_form_not_valid(self):
        form = OrderForm({
            'full_name': 'Luis Pena',
            'email': 'jansgreen@gmail.com',
            'phone_number': '19172130000',
            'street_address': '24 hughes Ave',
            'town_or_city': 'Bronx',
            'postcade': '10452',
            'country': 'USA',
            'county': 'NY',
        })
        self.assertFalse(form.is_valid())

    def test_form(self):
        form = OrderForm({})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)