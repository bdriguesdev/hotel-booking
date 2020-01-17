from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreateRoom.as_view()),
    path('delete/', views.EditRoom.as_view()),
    path('edit/', views.EditRoom.as_view()),
    path('add_amenities/', views.AddMultipliesAmenitiesToRoom.as_view()),
    path('remove_amenities/', views.RemoveMultipliesAmenitiesFromRoom.as_view()),
    path('details/', views.OneRoomDetails.as_view()),
    path('popular/', views.MostPopularRooms.as_view()),
    path('most_rated/', views.MostRatedRooms.as_view()),
    path('search/price_range/', views.PriceRangeRoomSearch.as_view()),
    path('search/all/', views.MultipliesQueriesRoomSearch.as_view()),
    path('hotel/', views.getAllHotelRooms.as_view()),
    path('test/', views.Test.as_view()),
    path('image_upload/', views.RoomImageUploader.as_view())
]