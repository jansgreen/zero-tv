from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    readonly_fields = (
        'user',
        'default_phone_number',
        'default_country',
        'default_postcade',
        'default_town_or_city',
        'default_street_address',
        'default_county',
        )

    fields = (
        'user',
        'default_phone_number',
        'default_country',
        'default_postcade',
        'default_town_or_city',
        'default_street_address',
        'default_county',
        )
    
    list_display = (
        'user',
        'default_phone_number',
        'default_country',
        'default_postcade',
        'default_town_or_city',
        'default_street_address',
        'default_county',
        )


admin.site.register(UserProfile, UserProfileAdmin)