from django import forms
from .widgets import CustomClearableFileInput
from .models import Movies, Genders, Classification

## THIS CODE COME FROM Boutique Ado ADJUSTED TO MY PROJECT
class ProductForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = '__all__'

    def __init__(self, *args, **kwargs):

        
        super().__init__(*args, **kwargs)
        Gender = Genders.objects.all()
        name = [(c.id, c.name) for c in Gender ]
        if self.fields['genre_ids']:
            self.fields['genre_ids'].choices = name
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] =  'border-black rounded-0'
        
        Cl_age = Classification.objects.all()
        age = [(c.id, c.minimum_age) for c in Cl_age ]
        if self.fields['sorting']:
            self.fields['sorting'].choices = age
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] =  'border-black rounded-0'


            
