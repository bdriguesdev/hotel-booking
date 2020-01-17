from django.db import models

from backend.hotel.models import Hotel
from backend.product.models import ProductList

def room_directory_path(instance, filename):
    return 'rooms/{0}/{1}'.format(instance, filename)

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField()
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.CASCADE)
    productList = models.ForeignKey(ProductList, related_name='rooms', on_delete=models.CASCADE, null=True)
    created = models.DateTimeField()
    updated = models.DateTimeField()
    reviews_count = models.IntegerField(default=0)
    reviews_total = models.IntegerField(default=0)
    reviews_average = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    #fields for promotion start and end and % -> maybe a new table for promotions? seems more accurate

    def __str__(self):
        return self.name

class RoomImage(models.Model):
    photo = models.ImageField(upload_to=room_directory_path)
    priority = models.IntegerField(default=0)
    room = models.ForeignKey(Room, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room.id)

class Amenity(models.Model):
    name = models.CharField(max_length=20)
    rooms = models.ManyToManyField(Room, related_name='amenities')

    def __str__(self):
        return self.name
