from django.urls import path 

from .views import (ViewTheatre, AddTheatre, 
                    TheatreDetail, EditTheatre,
                    RemoveTheatre)
                    

urlpatterns = [
    path('', ViewTheatre.as_view(), name='view_theatres'),
    path('add/', AddTheatre.as_view(), name ='add_theatre'),
    path('<int:pk>/', TheatreDetail.as_view(), name ='theatre_detail'),
    path('edit/<int:pk>/',EditTheatre.as_view(), name='edit_theatre'), 
    path('del/<int:pk>/', RemoveTheatre.as_view(), name='del_theatre') 
]