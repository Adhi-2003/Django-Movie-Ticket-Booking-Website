
from django.shortcuts import render 
from django.urls import reverse_lazy

# Create your views here.
from .models import Show
from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView) 

# custom form
from .forms import ShowForm


# -----------Show CRUD-----------------
class AddShow(CreateView):
    model = Show
    form_class = ShowForm
    template_name = 'show/show_create.html'
    success_url = reverse_lazy("view_shows")

class ViewShow(ListView):
    model = Show
    context_object_name = 'shows'
    template_name = 'show/show_list.html'

class ShowDetail(DetailView):
    model = Show
    context_object_name = 'show'
    template_name = 'show/show_detail.html'

class EditShow(UpdateView):
    model = Show
    fields = '__all__'
    template_name = 'show/show_update.html'
    success_url = reverse_lazy('view_shows')

class RemoveShow(DeleteView):
    model = Show
    template_name = 'show/show_delete.html'
    success_url = reverse_lazy('view_shows')