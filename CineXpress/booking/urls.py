from django.urls import path
from .views import SeatSelectionView, ConfirmBookingView, BookingDetailView, CancelBookingView, BookingListView

urlpatterns = [
    path('show/<int:show_id>/book/', SeatSelectionView.as_view(), name='book_seats'),
    path('show/<int:show_id>/confirm/', ConfirmBookingView.as_view(), name='confirm_booking'),
    path('<int:pk>/', BookingDetailView.as_view(), name='booking_detail'),
    path('<int:pk>/cancel/', CancelBookingView.as_view(), name='cancel_booking'),
    path('my-bookings/', BookingListView.as_view(), name='booking_list'),
    path('ticket/<int:pk>/', BookingDetailView.as_view(), name='ticket_details'),

]
