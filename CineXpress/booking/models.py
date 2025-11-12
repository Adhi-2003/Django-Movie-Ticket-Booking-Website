from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from show.models import Show
from theatre.models import Seat


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    payment_status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('completed', 'Completed'),
            ('failed', 'Failed'),
        ],
        default='pending'
    )

    def __str__(self):
        return f"Booking #{self.id} - {self.user.username} ({self.show})"

    @property
    def screen(self):
        return self.show.screen

    @property
    def movie(self):
        return self.show.movie

    def calculate_total_amount(self):
        """Calculates total price = number of seats * show price."""
        seat_count = self.booking_seats.count()
        self.total_amount = self.show.price * seat_count
        self.save(update_fields=['total_amount'])
        return self.total_amount
        

class BookingSeat(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='booking_seats')
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='booking_seats')
    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    class Meta:
        unique_together = ('booking', 'seat')

    def __str__(self):
        return f"{self.name} - {self.seat} (Booking #{self.booking.id})"

    def clean(self):
        """Ensure seat isn’t double-booked for the same show."""
        # Get the show for the current booking
        show = self.booking.show

        # Check if this seat is already booked in another booking for the same show
        conflict = BookingSeat.objects.filter(
            seat=self.seat,
            booking__show=show
        ).exclude(id=self.id).exists()

        if conflict:
            raise ValidationError(f"Seat {self.seat.number} is already booked for this show!")

    def save(self, *args, **kwargs):
        # Run validation before saving
        self.full_clean()
        super().save(*args, **kwargs)
        # Update total after adding a seat
        self.booking.calculate_total_amount()
