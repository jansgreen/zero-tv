from django.urls import path, include
from catalog.views import index

from . import views

urlpatterns = [
    path('', index, name='bag'),
    path('<int:id_movie>', views.id_movie, name='id_movie'),
    path('<movie_title>', views.a_movie, name='a_movie'),
    path('add/<int:id_movie>', views.push_bag, name='push_bag'),
    path('updata/<int:Movies_id>', views.updata, name='updata'),
    path('bag/save_movies', views.save_movies, name='save_movies'),



]


