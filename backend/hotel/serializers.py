from rest_framework import serializers

from backend.room.models import Room
from .models import Hotel, HotelImage

#This is here because of circle importing, if I import this from room.serializers it will broke the server
class RoomSimpleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['name', 'description', 'price', 'reviews_count', 'reviews_total', 'reviews_average']

class HotelImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = HotelImage
        fields = ['photo', 'priority', 'hotel']

class HotelSerializer(serializers.ModelSerializer):
    photos = HotelImageSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['name', 'id', 'description', 'photos', 'city', 'state', 'number', 'business']

class HotelWithRoomsDetailsSerializer(serializers.ModelSerializer):
    rooms = RoomSimpleSerializer(many=True)
    photos = HotelImageSerializer(many=True)

    class Meta:
        model = Hotel
        fields = ['name', 'id', 'rooms', 'photos', 'description', 'city', 'state', 'number', 'business']

