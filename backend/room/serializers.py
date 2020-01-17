from rest_framework import serializers

from backend.hotel.serializers import HotelSerializer
from .models import Room, Amenity, RoomImage

class RoomImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RoomImage
        fields = ['room', 'priority', 'photo']

class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer()
    photos = RoomImageSerializer(many=True)

    class Meta:
        model = Room
        fields = ['id', 'name', 'photos', 'description', 'price', 'hotel', 'reviews_count', 'reviews_total', 'reviews_average']

class AmenitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenity
        fields = ['name']