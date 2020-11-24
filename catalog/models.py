from django.db import models

# THIS CODE DOES NOT COME EXACTLY FROM A TUTORIAL, THIS IS THE RESULT OF SEVERAL TUTORIALS TO BE ABLE TO UNDERSTAND HOW THE MODELS RELATIONAL WORK.


from django.urls import reverse  # To generate URLS by reversing URL patterns


class Genders(models.Model):

    class Meta:
        verbose_name_plural = 'Genders'

    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
       
# Create your models here.
class Movies(models.Model):

    class Meta:
        verbose_name_plural = 'Movies'

    popularity = models.IntegerField(default=0, null=True, blank=True)
    vote = models.IntegerField(default=0, null=True, blank=True)
    video = models.BooleanField(default=False, null=True, blank=True)
    poster = models.URLField(max_length=1024, null=True, blank=True)
    adult =models.BooleanField(default=False, null=True, blank=True)
    backdrop =models.URLField(max_length=1024, null=True, blank=True)
    Language =models.CharField(max_length=5, null=True, blank=True)
    original_title =models.CharField(max_length=254, null=True, blank=True)
    genre_ids = models.ManyToManyField('Genders')
    title =models.CharField( max_length=254, null=True, blank=True)
    vote_average = models.IntegerField(default=0, null=True, blank=True)
    overview = models.TextField(max_length=554, null=True, blank=True)
    release_date =models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)


    
    def __str__(self):
        return self.title

    def get_date(self):
        return self.release_date