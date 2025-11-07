from django.db import models 

from django.core.validators import MinValueValidator, MaxValueValidator  
from django.utils.timezone import now

class Movie(models.Model):
    # Genre choices
    GENRE_CHOICES = [
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('drama', 'Drama'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('sci-fi', 'Science Fiction'),
        ('horror', 'Horror'),
        ('animation', 'Animation'),
        ('adventure', 'Adventure'),
        ('fantasy', 'Fantasy'),
        ('documentary', 'Documentary'),
        ('crime', 'Crime'),
        ('sports', 'Sports'),
        ('epic', 'Epic'),
        ('mystery', 'Mystery'),
        ('family', 'Family'),

    ]

    # Language choices
    LANGUAGE_CHOICES = [
        ('english', 'English'),
        ('hindi', 'Hindi'),
        ('tamil', 'Tamil'),
        ('telugu', 'Telugu'),
        ('malayalam', 'Malayalam'),
        ('kannada', 'Kannada'),
        ('french', 'French'),
        ('spanish', 'Spanish'),
        ('japanese', 'Japanese'),
        ('korean', 'Korean'),
    ]

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=50)
    actors = models.CharField(max_length=200)
    music_composer = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES,)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")

    
    release_date = models.DateField(default=now)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES)
    description = models.TextField()
    poster = models.ImageField(upload_to='movies/posters/')
    youtube_trailer = models.CharField(max_length=500, help_text="YouTube trailer URL")

    def get_duration(self):
        h, m = divmod(self.duration, 60)
        return f"{h}h {m}m" if h else f"{m}m"


    def __str__(self):
        return self.title
    
    @property
    def is_running(self):
        return True if self.shows.all() else False


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name= 'ratings')
    comment = models.CharField(max_length=50)
    # IMDb-style rating (e.g., 8.5)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(10.0)
        ],
        help_text="Movie rating out of 10 (e.g., 8.5)"
    )
    
    # we are going to link this with user