from rest_framework import serializers

from .models import Product, ProductList

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'price', 'description']

class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductList
        fields = ['name', 'products']