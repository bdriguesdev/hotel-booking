from rest_framework import serializers

from ..room.serializers import RoomSerializer
from ..auth_app.serializers import ClientSerializer
from .models import Booking, DiscountCoupon, Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['description', 'value', 'created']

class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    review = ReviewSerializer()
    client = ClientSerializer()
    
    class Meta:
        model = Booking
        fields = ['id', 'client', 'total_price', 'review', 'created', 'nights', 'start', 'end', 'room']

class BookingCalendarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = ['start', 'end']

class DiscountCouponSerializer(serializers.ModelSerializer):

    class Meta:
        model = DiscountCoupon
        fields = ['coupon']

class ReviewRoomSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    booking = BookingCalendarSerializer()

    class Meta:
        model = Review
        fields = ['description', 'value', 'created', 'booking', 'client']

