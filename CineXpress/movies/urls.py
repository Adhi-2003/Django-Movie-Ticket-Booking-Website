from django.urls import path 

from .views import (ViewMovies, AddMovie, 
                    MovieDetail, EditMovie,
                    RemoveMovie)
                    

urlpatterns = [
    path('', ViewMovies.as_view(), name='view_movies'),
    path('add/', AddMovie.as_view(), name = 'add_movie'),
    path('<int:pk>/', MovieDetail.as_view(), name = 'movie_detail'),
    path('edit/<int:pk>/',EditMovie.as_view(), name='edit_movie'), 
    path('del/<int:pk>/', RemoveMovie.as_view(), name='del_movie') 
]