from rest_framework import serializers

from .models import Client, Business

class ClientSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField()

    class Meta:
        model = Client
        fields = ['id', 'photo', 'first_name', 'last_name', 'birthday', 'city', 'state']

class BusinessSerializer(serializers.ModelSerializer):

    class Meta:
        model = Business
        fields = ['id', 'photo', 'name', 'email', 'city', 'state']