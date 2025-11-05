# URL routing for mainapp
from django.urls import path # type: ignore

from .views import homeView, aboutView, contactView
from .views import  (AddCarouselImage, 
                     ViewCarouselImages,
                     EditCarousel,
                     RemoveCarousel)

urlpatterns = [
    path('', homeView, name='home_page'),

    # Create
    path('carousel/add/', AddCarouselImage.as_view(), name='add_carousel'),
    # Read
    path('carousel/all/', ViewCarouselImages.as_view(), name='carousels_page'),
    # Update
    path('carousel/edit/<int:pk>', EditCarousel.as_view(), name='edit_carousel'),
    # Delete
    path('carousel/del/<int:pk>', RemoveCarousel.as_view(), name='del_carousel'),
    


    path('about', aboutView, name='about_page'),
    path('contact', contactView, name='contact_page')
]
