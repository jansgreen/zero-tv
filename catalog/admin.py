
from django.contrib import admin
from .models import Movies,  Genders

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'adult',
        'poster',
        'overview',
        'release_date',
    )

    ordering = ('release_date',)


class GendersAdmin(admin.ModelAdmin):
    fields = ['id','name']
    list_display = (
        'pk',
        'name',
    )
    
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Genders, GendersAdmin)