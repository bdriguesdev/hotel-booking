from django.db import models

def client_directory_path(instance, filename):
    return 'clients/{0}/{1}'.format(instance, filename)

def business_directory_path(instance, filename):
    return 'businesses/{0}/{1}'.format(instance, filename)

class Client(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=50)
    birthday = models.DateTimeField()
    email = models.EmailField(unique=True, max_length=50)
    password = models.CharField(max_length=80)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=35)
    photo = models.ImageField(upload_to=client_directory_path)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    def __str__(self):
        return str(self.id)

class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=30)
    photo = models.ImageField(upload_to=business_directory_path)
    created = models.DateTimeField()
    updated = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Businesses"

    def __str__(self):
        return str(self.id)
