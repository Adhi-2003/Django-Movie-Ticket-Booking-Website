from django.contrib import admin

# Register your models here.
from .models import Theatre, TheatreScreen, Seat


admin.site.register(Theatre)
admin.site.register(TheatreScreen)
admin.site.register(Seat)