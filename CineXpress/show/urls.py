from django.urls import path 

from .views import (ViewShow, AddShow, 
                    ShowDetail, EditShow,
                    RemoveShow)
                    

urlpatterns = [
    path('', ViewShow.as_view(), name='view_shows'),
    path('add/', AddShow.as_view(), name ='add_show'),
    path('<int:pk>/', ShowDetail.as_view(), name ='show_detail'),
    path('edit/<int:pk>/',EditShow.as_view(), name='edit_show'), 
    path('del/<int:pk>/', RemoveShow.as_view(), name='del_show') 
]