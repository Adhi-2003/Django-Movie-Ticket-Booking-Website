from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.urls import reverse
from show.models import Show
from theatre.models import Seat
from .models import Booking, BookingSeat
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class SeatSelectionView(LoginRequiredMixin, View):
    """Display available seats for a specific show."""
    template_name = 'booking/book_seats.html'

    def get(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        seats = Seat.objects.filter(theatre_screen=show.screen)

        # Seats already booked for this show
        booked_seat_ids = BookingSeat.objects.filter(
            booking__show=show
        ).values_list('seat_id', flat=True)

        # Organize by row label (e.g., 'A', 'B', 'C')
        seat_map = {}
        for seat in seats:
            row = seat.number[0].upper()
            seat_map.setdefault(row, []).append(seat)

        context = {
            'show': show,
            'seat_map': seat_map,
            'booked_seat_ids': list(booked_seat_ids),
        }
        return render(request, self.template_name, context)


class ConfirmBookingView(LoginRequiredMixin, View):
    """Handle seat selection and create booking."""
    def post(self, request, show_id):
        show = get_object_or_404(Show, id=show_id)
        selected_seats = request.POST.get('selected_seats', '').split(',')
        selected_seats = [s for s in selected_seats if s]

        if not selected_seats:
            messages.error(request, "Please select at least one seat.")
            return redirect(reverse('book_seats', args=[show.id]))

        # Validate seat availability
        already_booked = BookingSeat.objects.filter(
            booking__show=show,
            seat_id__in=selected_seats
        ).exists()
        if (already_booked):
            messages.error(request, "Some seats are already booked. Please refresh and try again.")
            return redirect(reverse('book_seats', args=[show.id]))

        # Create booking atomically
        with transaction.atomic():
            booking = Booking.objects.create(
                user=request.user,
                show=show,
                payment_status='pending'
            )

            for seat_id in selected_seats:
                seat = get_object_or_404(Seat, id=seat_id)

                name = request.POST.get(f'viewer_name_{seat_id}') or request.user.username
                dob = request.POST.get(f'viewer_dob_{seat_id}') or "2000-01-01"
                gender = request.POST.get(f'viewer_gender_{seat_id}') or "other"

                BookingSeat.objects.create(
                    booking=booking,
                    seat=seat,
                    name=name,
                    dob=dob,
                    gender=gender
                )

            booking.calculate_total_amount()

        messages.success(request, f"Booking successful! Total: ₹{booking.total_amount}")
        return redirect(reverse('payment:create_razorpay_order', args=[booking.id]))


from django.views.generic import DetailView

class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking/booking_confirm.html'
    context_object_name = 'booking'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        booking = self.get_object()
        # URL to Razorpay payment
        context['payment_url'] = reverse('payment:create_razorpay_order', args=[booking.id])
        return context
    

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.contrib import messages


class CancelBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'booking/booking_cancel_confirm.html'
    context_object_name = 'booking'

    def delete(self, request, *args, **kwargs):
        booking = self.get_object()
        
        # If you want to free up the seats (optional)
        for seat in booking.booking_seats.all():
            seat.seat.is_available = True
            seat.seat.save()
            seat.delete()  # remove the link between booking and seat
        
        messages.success(request, f'Booking for "{booking.movie.title}" has been cancelled successfully.')
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('home_page') + '#movie_list'

class BookingListView(LoginRequiredMixin, ListView):
    model = Booking
    template_name = 'booking/booking_list.html'
    context_object_name = 'bookings'
    login_url = 'login'  # Redirects if not logged in

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user).select_related('show__movie', 'show__screen').order_by('-id')



class BookingDetailView(LoginRequiredMixin, DetailView):
    model = Booking
    template_name = 'booking/booking_detail.html'
    context_object_name = 'booking'

    def get_object(self, queryset=None):
        """Ensure user can only see their own booking"""
        return get_object_or_404(Booking, id=self.kwargs['pk'], user=self.request.user)
