from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('gendres', views.Upload_gendres, name='Upload_gendres'),
    path('movies', views.Upload_Movies, name='Upload_Movies'),
    path('account', include('allauth.urls')),
    path('add/', views.add_Movies, name='add_Movies'),
    path('edit/<int:Movies_id>/', views.edit_Movie, name='edit_Movie'),
    path('delete/<int:Movies_id>/', views.delete_Movie, name='delete_Movie'),
    path('Manual', views.Manual, name='Manual'),



  ]
