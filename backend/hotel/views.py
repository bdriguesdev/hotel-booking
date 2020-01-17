from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models import Q
from django.utils import timezone

from .serializers import HotelSerializer, HotelWithRoomsDetailsSerializer, HotelImageSerializer
from ..validators import textValidator, stateValidator, cityValidator, intValidator
from .models import Hotel, HotelImage

class CreateHotel(APIView):

    def post(self, request):
        try:
            if request.authorized == False:
                return Response('Acess denied.')
            if request.user_type != 'Business':
                return Response('Acess denied.')

            name = textValidator(request.data['hotelName'], 30, 3)
            description = textValidator(request.data['description'], 450, 10)
            city = cityValidator(request.data['city']) #need to validate
            state = stateValidator(request.data['state'])
            # neighborhood = request.data['neighborhood'] #need to validate
            complement = request.data['complement'] #need to validate
            business = request.authorized
            number = intValidator(int(request.data['number'])) #need to create a better validation, if the number is 0 means this doesn't have number. This also can be letters....

            hotel = Hotel(name=name, description=description, city=city, state=state, complement=complement, business=business, number=number, created=timezone.now(), updated=timezone.now())
            hotel.save()

            serializer = HotelSerializer(hotel)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class DeleteHotel(APIView):

    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception
            
            hotel_id = intValidator(request.data['id'])
            hotel = Hotel.objects.filter(id=hotel_id)

            if hotel.business != request.authorized: #this will work?
                return Response('Acess denied.')
            hotel.delete()
            #when booking-app is created do I need to cancel this action if the hotel was a booking occuring? Or even a booking scheduled?
            #the best idea here is to return a message informing that the business need to be in contact to the support to be able to delete the hotel in this circumstances

            return Response(hotel)
        except Exception:
            return Response('Send a valid data.')

class HotelImageUploader(APIView):

    def put(self, request):    
        try:
            hotel_id = request.data['hotelId']
            priority = request.data['priority']
            print(request.data['hotelId'])
            hotel = Hotel.objects.get(id=hotel_id)
            print('here2')
            if hotel.business.id != request.authorized.id:
                raise Exception("You don't have permission to modify hotels that aren't ours.")

            hotel_image = HotelImage(photo=request.FILES['photo'], priority=priority, hotel=hotel)
            hotel_image.save()
            
            serializer = HotelImageSerializer(hotel_image)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response(str(err))

class getHotelImages(APIView):

    def post(self, request):
        try:
            hotel_id = request.data['hotelId']
            hotel_images = HotelImage.objects.filter(hotel_id=hotel_id)

            serializer = HotelImageSerializer(hotel_images, many=True)

            return Response(serializer.data)
        except Exception as err:
            return Response(str(err))

class AllUserHotels(APIView):

    def get(self, request):
        try:
            if request.authorized == False or request.user_type != "Business":
                raise Exception("You don't have permission.")

            # hotels = Hotel.objects.filter(business_id=request.authorized.id)
            hotels = Hotel.objects.all()
            serializer = HotelSerializer(hotels, many=True)

            return Response(serializer.data)
        except Exception as err:
            return Response(str(err))

#update Hotel ?

class OneHotelDetails(APIView):

    def post(self, request):
        try:
            hotel_id = request.data['hotelId']
            hotel = Hotel.objects.get(id=hotel_id)
            hotel.views += 1
            hotel.save()
            serializer = HotelSerializer(hotel)

            return Response(serializer.data)
        except Exception:
            return Response('An error has been occurred.')

class MostPopularHotels(APIView):

    def get(self, request):
        try:
            hotels = Hotel.objects.order_by('-views')[0:4]
            serializer = HotelSerializer(hotels, many=True)
            
            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('Send a valid data.')

class MultipliesQueriesHotelSearch(APIView):

    def post(self, request):
        try:
            hotels = Hotel.objects

            if request.data['businessSearch'] == 'True':
                business_id = request.data['businessId']
                hotels = hotels.filter(business_id=business_id)

            if request.data['nameSearch'] == 'True':
                name = textValidator(request.data['name'], 30, 3)
                hotels = hotels.filter(name__contains=name)

            # if request.data['reviewsSearch'] == 'True':
            #     reviews_min = request.data['minReview'] #validate
            #     reviews_max = request.data['maxReview'] #validate

            #     hotels = hotels.filter(Q(reviews_average__gte=reviews_min) & Q(reviews_average__lte=reviews_max))

            if request.data['citySearch'] == 'True':
                city = request.data['city']
                hotels = hotels.filter(city__contains=city)

            if request.data['stateSearch'] == 'True':
                state = request.data['state']
                hotels = hotels.filter(state__contains=state)
            
            serializer = HotelSerializer(hotels, many=True)

            return Response(serializer.data)
        except Exception as err:
            return Response(str(err))