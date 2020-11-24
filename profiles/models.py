from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver

#    This code come from Boutique ado, if you wanna see my db relational go to catalog models
class UserProfile(models.Model):
    """
    UserProfile informations
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=11, null=True, blank=True)
    default_country = CountryField()
    default_postcade = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city =models.CharField(max_length=40, null=True, blank=True)
    default_street_address =models.CharField(max_length=80, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} UserProfile'


    @receiver(post_save, sender=user)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(User=instance)
        instance.UserProfile.save()
