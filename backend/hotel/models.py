from django.db import models

from backend.auth_app.models import Business

def hotel_directory_path(instance, filename):
    return 'hotels/{0}/{1}'.format(instance, filename)

class Hotel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    neighborhood = models.CharField(max_length=40)
    complement = models.CharField(max_length= 60)
    business = models.ForeignKey(Business, related_name='hotels', on_delete=models.CASCADE)
    number = models.IntegerField()
    views = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)
    reviews_total = models.IntegerField(default=0)
    reviews_average = models.IntegerField(default=0)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.name

class HotelImage(models.Model):
    photo = models.ImageField(upload_to=hotel_directory_path)
    priority = models.IntegerField(default=0)
    hotel = models.ForeignKey(Hotel, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.hotel.id)