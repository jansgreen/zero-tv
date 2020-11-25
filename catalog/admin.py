
from django.contrib import admin
from .models import Movies,  Genders, Classification

# Register your models here.

class MoviesAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'sorting',
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

class ClassificationAdmin(admin.ModelAdmin):
    fields = ['indicator','minimum_age', 'recommendation']
    list_display = (
        'pk',
        'indicator',
        'minimum_age',
        'recommendation',

    )
    
admin.site.register(Movies, MoviesAdmin)
admin.site.register(Genders, GendersAdmin)
admin.site.register(Classification, ClassificationAdmin)
