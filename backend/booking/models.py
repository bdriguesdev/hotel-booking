from django.db import models

from backend.room.models import Room
from backend.auth_app.models import Client

class Review(models.Model):
    #here do i need a validation for the value be between 1-5 ? 
    client = models.ForeignKey(Client, related_name='reviews', on_delete=models.CASCADE)
    value = models.FloatField()
    description = models.TextField(max_length=150)
    room = models.ForeignKey(Room, related_name='reviews', on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return str(self.client.id)

class DiscountCoupon(models.Model):
    coupon = models.CharField(max_length=20)
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    expire = models.DateTimeField()
    created = models.DateTimeField()
    used_by = models.ForeignKey(Client, related_name='coupons', on_delete=models.CASCADE)

    def __str__(self):
        return self.coupon

class RoomPromotion(models.Model):
    room = models.ForeignKey(Room, related_name='promotions', on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    min_price = models.IntegerField(default=0)
    max_price = models.IntegerField(default=0)
    percentage = models.IntegerField(default=0)
    value = models.IntegerField(default=0)
    created = models.DateTimeField()

    def __str__(self):
        return self.room.name

class Booking(models.Model):
    client = models.ForeignKey(Client, related_name='bookings', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.CASCADE)
    total_price = models.FloatField()
    created = models.DateTimeField()
    nights = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    review = models.OneToOneField(Review, related_name='booking', on_delete=models.CASCADE, null=True)
    coupon = models.ForeignKey(DiscountCoupon, related_name='bookings', on_delete=models.CASCADE, null=True)
    promotion = models.ForeignKey(RoomPromotion, related_name='bookings', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.client.id)
