from django.shortcuts import render, redirect, reverse
from .models import Movies, Genders, Classification
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib import messages
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
#from django.urls import reverse
import datetime
import json
from django.contrib.auth.decorators import permission_required
from . import API
import random
import os


from django.urls import reverse_lazy
from .forms import ProductForm

# ALL THE FOLLOWING CODES WERE OF MY OWN WITNESS, FOLLOWING TUTORIAL INSTRUCTIONS ON YOUTUBE .


def index(request):
    """ A view to show all products, including sorting and search queries """ 
    print(os.path.abspath(__file__))
    search = request.GET.get("Search")
    galeries = Movies.objects.all().order_by('title')
    if search:
        galeries = Movies.objects.filter(
            Q(title__icontains = search) | Q(release_date__icontains = search) | Q(pk__icontains = search)
            ).distinct()
        if not galeries:
            messages.warning(request, f'The movie {search} you looking far is not found!')
            
    paginator = Paginator(galeries, 20)
    if paginator:
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            }
        return render(request, 'index.html', context)
    else:
        messages.error(request, f'we not have any movies, please contact the own')
        return redirect('index')



def Upload_Movies(request):
    """
    Update the movies json flie
    """
    api = API.get_movies()
    messages.success(request, f'the movie database update successfully')
    return redirect('index')

def Upload_gendres(request):
    """
    Update the genres json flie

    """
    api = API.get_gendres()
    return redirect('index')
 

@login_required
def add_Movies(request):
    """
    Add the new movie to catalog
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Movie = form.save()
            messages.success(request, 'Movie was added successfully!')
            return redirect(reverse('a_movie', args=[Movies.title]))
        else:
            messages.error(request, 'faild to add Movie!')
    else:
        form = ProductForm()
 
    template = 'catalog/add_Movie.html'
    context = {
        'form': form,

    }

    return render(request, template, context)

@login_required
def edit_Movie(request, Movies_id):
    """
    Edit a movie exist
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only person autorizate can edit movies')
        return redirect(reverse('home'))
    movie= get_object_or_404(Movies, pk=Movies_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, reuqest.FILES, instance=Movies)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully updated Movie!')
        else:
            messages.success(request, 'Failed to updated Movie!')
    else:
        form = ProductForm(instance=Movies)
        messages.info(request, f'You are editing {Movies.title}')

    template = 'catalog/edit_Movie.html'
    context = {
        'form':form,
        'Movies': movie,

    }
    return render(request, template, context)

@login_required
def delete_Movie(request, Movies_id):
    """
    Edit a movie exist
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only person autorizate can delete movies')
        return redirect(reverse('home'))
    movie= get_object_or_404(Movies, pk=Movies_id)
    movie.delete()
    messages.success(request, 'Movie delete successfully!')
    return redirect(reverse('index'))


def Manual(request):
    genres_append =[]
    with open("catalog/fixtures/movie.json") as Movie_data:
        Movies_json = json.load(Movie_data)
        for Movie_loaded in Movies_json:
            if "adult" in Movie_loaded["fields"]:
                if Movie_loaded["fields"]["title"].upper() == "XXX" or Movie_loaded["fields"]["title"].upper() == "PORN" or Movie_loaded["fields"]["title"].upper() == "SEX" or Movie_loaded["fields"]["adult"] == "true" :
                    classification = Classification.objects.get(pk=5)
                else:
                    age_classification = random.randint(1, 4)
                    classification = Classification.objects.get(pk=age_classification)

                data = Movies.objects.create(

                    popularity = Movie_loaded["fields"]["popularity"],  
                    vote = Movie_loaded["fields"]["vote"],
                    video = Movie_loaded["fields"]["video"],
                    poster = Movie_loaded["fields"]["poster"],
                    sorting = classification,
                    backdrop = Movie_loaded["fields"]["backdrop"],
                    language = Movie_loaded["fields"]["Language"],
                    original_title =  Movie_loaded["fields"]["original_title"],
                    title = Movie_loaded["fields"]["title"],
                    vote_average = Movie_loaded["fields"]["vote_average"],
                    overview = Movie_loaded["fields"]["overview"],
                    release_date = Movie_loaded["fields"]["release_date"],
                    price = Movie_loaded["fields"]["price"],

                    )

            if "genres_ids" in Movie_loaded["fields"]:
                for genres_ids in Movie_loaded["fields"]["genres_ids"]:
                    genres = Genders.objects.get(pk=genres_ids)
                    data.genre_ids.set([genres])
            data.save()
    messages.success(request, f'The movie Database is upload successfully')
    return redirect(reverse('index'))













