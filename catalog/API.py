import os
import json
import requests
from django.http import HttpResponse
from .models import Movies, Genders
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.conf import settings


# Search GitHub's repositories for requests

class Url_api:
    def __init__ (self, url):
        self.url = url


    def discover(self):
        Str_Theater = []
        num = 0
        api_url = 'https://api.themoviedb.org'
        api_key = settings.API_KEY
        url_page = requests.get(str(api_url)+str(self.url)+str(api_key)).text
        if self.url == "/3/discover/movie?":
            total_pages = json.loads(url_page)
            pages = int(total_pages["total_pages"]) - 30 
            for page in range(1, pages):
                lib = requests.get(str(api_url)+str(self.url)+str(api_key), params={'page':page}).text
                lib_movie = json.loads(lib)
                Str_Theater.append(lib_movie)
            Theater = Str_Theater
            return Theater
        elif self.url == "/3/genre/movie/list?":
            lib = requests.get(str(api_url)+str(self.url)+str(api_key)).text
            lib_movie = json.loads(lib)
            Str_Theater.append(lib_movie)
            Theater = Str_Theater
            return Theater

            



def get_movies(): # this functios make complete the url API
    url = "/3/discover/movie?"
    get_url = Url_api(url)
    Theater = get_url.discover()
    movie_json = Theater

    data = movie_json
    Name_data = "movie"
    set_data = mk_data(data, Name_data)
    def_data = set_data.mk_field()

class mk_data():
    def __init__(self, data, Name_data):
        self.data = data
        self.Name_data = Name_data
    
    
    def mk_field(self):
        theater=[]
        genres=[]
        genres_pk=[]
        full_data = self.data
        x = 0
        for result in full_data:
            obj_movie = result["results"]
            for movie in obj_movie:
                x +=1
                popularity = movie['popularity']
                vote = movie['vote_count']
                video = movie['video']
                poster = movie['poster_path']
                adult =  movie['adult']
                backdrop = movie['backdrop_path']
                Language = movie['original_language']
                original_title = ['original_title']
                title =  movie['title']
                vote_average = movie['vote_average']
                overview = movie['overview']
 
                if 'release_date' in movie:
                    date = movie['release_date']
                    if date == "":
                        release_date = "2020-01-01"

                    elif datetime.strptime(date,'%Y-%m-%d'):
                        release_date = date
                    else:
                        release_date = "2020-01-01"
                else:
                    release_date = "2000-01-01"


                if int(popularity) > 0 | int(vote_average) > 0 :
                    price = round((popularity/vote_average)* 2.5, 2)
                else:
                    price = round((20/10)* 2.5, 2)
                

                data = Movies.objects.create(
                    popularity=popularity,  
                    vote = vote,
                    video = video,
                    poster = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+str(poster),
                    adult = adult,
                    backdrop = 'https://image.tmdb.org/t/p/w600_and_h900_bestv2'+str(backdrop),
                    Language = Language,
                    original_title = original_title,
                    title = title,
                    vote_average = vote_average,
                    overview = overview,
                    release_date = release_date,
                    price = price,

                    )
                if 'genre_ids' in movie:
                    genres_form = movie['genre_ids']
                    for genres_numbers in range(len(genres_form)):
                        genres = Genders.objects.filter(Q(pk=int(genres_form[genres_numbers])))
                        data.genre_ids.set(genres)
                data.save()                        


def get_gendres(): # this functios make complete the url API
    url = "/3/genre/movie/list?"
    get_url = Url_api(url)
    Theater = get_url.discover()
    movie_json = Theater

    data = movie_json
    Name_data = "Genders"
    set_data = mk_data_gendres(data, Name_data)
    def_data = set_data.mk_field()

class mk_data_gendres():
    def __init__(self, data, Name_data):
        self.data = data
        self.Name_data = Name_data

    def mk_field(self):
        theater=[]
        full_data = self.data
        x=0
        for result in full_data:
            obj_movie = result["genres"]
            for movie in obj_movie:
                id = movie['id']
                name = movie['name']
                x+=1
                theater.append({
                    "model": "catalog.Genders",
                    "pk": id,
                    "fields": {
#                        "Genders_id": id,
                        "name": name
                    }
                })
        url = str('./catalog/fixtures/')+str(self.Name_data)+str('.json')
        with open(url, 'w') as file:
            json.dump(theater, file, indent=4)
