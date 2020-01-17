from django.db import models

from backend.auth_app.models import Business

def room_directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.id, filename)

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    description = models.TextField(max_length=50)
    business = models.ForeignKey(Business, related_name='products', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=room_directory_path)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return self.name

class ProductList(models.Model):
    name = models.CharField(max_length=20)
    products = models.ManyToManyField(Product, related_name='product_lists')
    business = models.ForeignKey(Business, related_name='product_lists', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name