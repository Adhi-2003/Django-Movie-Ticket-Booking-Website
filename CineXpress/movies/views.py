
from django.shortcuts import render 
from django.urls import reverse_lazy

# Create your views here.
from .models import Movie, MovieRating
from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView) 

# -----------Movie CRUD-----------------
class AddMovie(CreateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_create.html'
    success_url = reverse_lazy("view_movies")

class ViewMovies(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/movies_list.html'

class MovieDetail(DetailView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/movie_detail.html'

class EditMovie(UpdateView):
    model = Movie
    fields = '__all__'
    template_name = 'movies/movie_update.html'
    success_url = reverse_lazy('view_movies')

class RemoveMovie(DeleteView):
    model = Movie
    template_name = 'movies/movie_delete.html'
    success_url = reverse_lazy('view_movies')