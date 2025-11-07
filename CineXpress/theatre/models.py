from django.db import models

# Create your models here.

class Theatre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    image = models.ImageField(upload_to='theatres/', null=True, blank=True)


    def __str__(self):
        return self.name
    
    @property
    def no_of_screens(self):
        return self.seats.count()
    
class TheatreScreen(models.Model):
    class ScreenType(models.TextChoices):
        STANDARD = "Standard", "Standard"
        THREE_D = "3D", "3D"
        IMAX = "IMAX", "IMAX"
        DOLBY_ATMOS = "Dolby Atmos", "Dolby Atmos"
        FOUR_K_ULTRA_HD = "4K Ultra HD", "4K Ultra HD"
        IMAX_DOLBY = "IMAX with Dolby", "IMAX with Dolby"
        SCREEN_X = "ScreenX", "ScreenX"
        PLF = "PLF (Premium Large Format)", "PLF (Premium Large Format)"
        GOLD_CLASS = "Gold Class", "Gold Class"


    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='screens')
    name = models.CharField(max_length=50, help_text="Example: Screen 1, Screen 2, etc.")
    type = models.CharField(max_length=50, choices=ScreenType.choices, default=ScreenType.STANDARD)

    def __str__(self):
        return f"{self.theatre.name} - {self.name} ({self.type})"
    
    @property
    def seat_count(self):
        return self.seats.filter(availability = True).count()

class Seat(models.Model):
    class SeatType(models.TextChoices):
        SILVER = "Silver", "Silver"
        GOLD = "Gold", "Gold"
        PLATINUM = "Platinum", "Platinum"
        RECLINER = "Recliner", "Recliner"
        COUPLE = "Couple", "Couple"
        VIP = "VIP", "VIP"
        LOUNGE = "Lounge", "Lounge"

    theatre_screen = models.ForeignKey('TheatreScreen', on_delete=models.CASCADE, related_name='seats')
    number = models.CharField(max_length=10)
    availability = models.BooleanField(default=True)
    type = models.CharField(max_length=20, choices=SeatType.choices, default=SeatType.SILVER)

    def __str__(self):
        return f"{self.number} ({self.type}) - {self.theatre_screen}"
