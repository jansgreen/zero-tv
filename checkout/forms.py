from django import forms
from .models import order
class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = (
            'full_name',
            'email',
            'phone_number',
            'street_address',
            'town_or_city',
            'postcade',
            'country',
            'county',
            )
            
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcade': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control stripe-style-input'
            self.fields[field].widget.attrs['aria-label'] = 'Sizing example input'
            self.fields[field].widget.attrs['aria-describedby'] = 'inputGroup-sizing-sm'
            self.fields[field].label = False