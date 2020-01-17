from django.urls import path

from . import views

urlpatterns = [
    path('booking/create/', views.CreateBooking.as_view()),
    path('booking/cancel/', views.CancelBooking.as_view()),
    path('review/create/', views.CreateReview.as_view()),
    path('promotion/create/', views.CreatePromotion.as_view()),
    path('booking/month/', views.getBookingsPerMonth.as_view()),
    path('booking/user/', views.getUserBookings.as_view()),
    path('review/room/', views.getRoomReviews.as_view()),
    path('review/hotel/', views.getReviewsAllRoomsFromHotel.as_view()),
    path('booking/hotel/', views.getHotelBookingsPerMonth.as_view()),
    path('booking/room/', views.getBookingsPerMonthWithDetails.as_view())
]