from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateHotel.as_view()),
    path('delete/', views.DeleteHotel.as_view()),
    path('details/', views.OneHotelDetails.as_view()),
    path('popular/', views.MostPopularHotels.as_view()),
    path('search/', views.MultipliesQueriesHotelSearch.as_view()),
    path('image_upload/', views.HotelImageUploader.as_view()),
    path('all/', views.AllUserHotels.as_view()),
    path('images/', views.getHotelImages.as_view())
]