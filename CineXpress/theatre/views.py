
from django.shortcuts import render 
from django.urls import reverse_lazy

# Create your views here.
from .models import Theatre
from django.views.generic import (CreateView, ListView, 
                                  DetailView, UpdateView, DeleteView) 

# -----------Theatre CRUD-----------------
class AddTheatre(CreateView):
    model = Theatre
    fields = '__all__'
    template_name = 'theatre/theatre_create.html'
    success_url = reverse_lazy("view_theatres")

class ViewTheatre(ListView):
    model = Theatre
    context_object_name = 'theatres'
    template_name = 'theatre/theatre_list.html'

class TheatreDetail(DetailView):
    model = Theatre
    context_object_name = 'theatre'
    template_name = 'theatre/theatre_detail.html'

class EditTheatre(UpdateView):
    model = Theatre
    fields = '__all__'
    template_name = 'theatre/theatre_update.html'
    success_url = reverse_lazy('view_theatres')

class RemoveTheatre(DeleteView):
    model = Theatre
    template_name = 'theatre/theatre_delete.html'
    success_url = reverse_lazy('view_theatres')