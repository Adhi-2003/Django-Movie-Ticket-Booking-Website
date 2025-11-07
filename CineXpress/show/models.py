from django.db import models 
from movies.models import Movie
from theatre.models import TheatreScreen

# Create your models here.

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    screen = models.ForeignKey(TheatreScreen, on_delete=models.CASCADE, related_name='shows')
    show_date = models.DateField()
    start_time = models.TimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('screen', 'show_date', 'start_time')
        ordering = ['show_date', 'start_time']

    def __str__(self):
        return f"{self.movie.title} - {self.screen.name} ({self.show_date} {self.start_time})"
