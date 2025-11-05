from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore

from .models import CarouselImage

# Create your views here.
def homeView(request):
    template_name = 'mainapp/home.html'
    context = {
        # dictionary with context data.
        'carousel_images' : CarouselImage.objects.all()
        # The above line is equalient to `SELECT * FROM CarouselImage;`

    }
    return render(request, template_name, context)

# Let's implement CRUD operations for Carousel Image using Class based views.

# Class Based Views are declarative methods to implement views.
# Because of OOPs, the programming style is very abstract i.e., implementation details
# are hidden. 
# These views, even though less detailed in readability, improves abstraction and 
# prevents Re-inventing the wheel, as classes can be inherited and their functionalities
# extended.
    # In Django, realizing the most common usages of request-response scenarios,
    # generic Class Based Views (CBVs) were created.
    # For Inserting new records of the given model into DB, 
        # 1. CreateView (Create)
    # For Querying all records of the given model from DB,
        # 2. ListView   (Read)
    # For Querying a specific record from the given model using pk,
        # 3. DetailView (Read)
    # For Updating or editing a specific record using pk,
        # 4. UpdateView (Update)
    # For Deleting a specific record using pk,
        # 5. DeleteView (Delete)
# ------------------

from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView # type: ignore


#-----------------------------Carousel CRUD-------------------------------
# Creating records - 
class AddCarouselImage(CreateView):
    model = CarouselImage # This provides table name for inserting records
    fields = '__all__' # Fields to insert values into
    # Defining where the site should redirect to, after successful insertion of record.
    success_url = reverse_lazy('carousels_page') # type: ignore

    template_name = 'mainapp/carousel_add.html'

# Reading
class ViewCarouselImages(ListView):
    model = CarouselImage
    context_object_name = 'carousel_images' # If not used, obj name will be <model_name>_list
    template_name = 'mainapp/carousel_list.html'

# Updating
class EditCarousel(UpdateView):
    model = CarouselImage
    template_name = 'mainapp/carousel_update.html'
    fields = '__all__'
    success_url = reverse_lazy('carousels_page')

# Delete
class RemoveCarousel(DeleteView):
    model = CarouselImage
    template_name = 'mainapp/carousel_delete.html'
    success_url = reverse_lazy('carousels_page')

# -----------------------------------------------------------------


def aboutView(request):
    template_name = 'mainapp/about.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name, context)

def contactView(request):
    template_name = 'mainapp/contact.html'
    context = {
        # dictionary with context data.
    }
    return render(request, template_name, context)
