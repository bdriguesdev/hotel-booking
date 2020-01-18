from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from django.utils import timezone

from backend.exceptions import CustomException
from .serializers import RoomSerializer, AmenitySerializer, RoomImageSerializer
from backend.validators import textValidator, numValidator, intValidator
from .models import Room, Amenity, RoomImage
from backend.hotel.models import Hotel

class CreateRoom(APIView):

    def post(self, request):
        try:
            if request.user_type != 'Business': 
                return Response('Acess denied.')
            hotel = Hotel.objects.get(id=request.data['hotelId']) 
            if request.authorized.id != hotel.business.id:
                return Response('Acess denied.')
            name = textValidator(request.data['name'], 40, 5)
            description = textValidator(request.data['description'], 450, 10)
            price = numValidator(request.data['price'], 1000, 5)
            
            room = Room(name=name, description=description, price=price, created=timezone.now(), hotel=hotel, updated=timezone.now())
            room.save()
            serializer = RoomSerializer(room)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error has been occurred.' })
        

class RemoveRoom(APIView):
    
    def delete(self, request):
        #need to check if a user has booked this room
        try:
            if request.user_type != 'Business':
                return Response('Acess denied.')
            
            room_id = intValidator(request.data['id'])
            room = Room.objects.filter(id=id)
            if room.hotel.business != request.authorized: #need to check here correctly
                return Response('Acess denied.')
            room.delete()

            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')
        
class EditRoom(APIView):

    def update(self, request):
        #need to verify if the user has this room is from one of his hotels
        #maybe do something if the query can't find the room?
        #if this doesn't work I need to search how to do this
        try:
            if request.user_type != 'Business':
                return Response('Acess denied')

            room_id = intValidator(request.data['id'])
            room = Room.objects.get(id=room_id)
            if room.hotel.business != request.authorized: #need to check here correctly
                return Response('Acess denied.')

            if request.data['nameEdit']:
                name = textValidator(request.data['name'], 40, 5)
                room.name = name
            if request.data['descriptionEdit']:
                description = textValidator(request.data['description'], 200, 10)
                room.description = description
            if request.data['priceEdit']:
                price = numValidator(request.data['price'], 5, 1000)
                room.price = price
            room.updated = timezone.now()
            room.save()
            
            serializer = RoomSerializer(room)
            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class getAllHotelRooms(APIView):

    def post(self, request):
        try:       
            hotel_id = request.data['hotelId']
            rooms = Room.objects.filter(hotel_id=hotel_id)

            serializer = RoomSerializer(rooms, many=True)

            return Response(serializer.data)
        except Exception:
            return Response({ "error": 'An error has been occurred.' })

#only admins can create perks

class AddMultipliesAmenitiesToRoom(APIView):

    #check if the business has the hotel/room and the perk exist
    def post(self, request):
        try:
            if request.user_type != 'Business':
                return Response('Acess denied')
            
            room_id = intValidator(request.data['id'])
            room = Room.objects.get(id=room_id)
            if room.hotel.business != request.authorized: #need to check here correctly
                return Response('Acess denied.')

            if len(request.data['amenities']) <= 0:
                raise Exception
            
            #here could have some problems if the room already have this perk, monkaHmm
            for x in range(0, len(request.data['amenities'])):
                if not(isinstance(request.data['amenities'][x], int)):
                    raise Exception
                amenity = Amenity.objects.get(id=request.data['amenities'][x])
                room.amenities.add(amenity)

            room.updated = timezone.now()
            room.save()
            serializer = RoomSerializer(room)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class RemoveMultipliesAmenitiesFromRoom(APIView):

    #check if the business has the hotel/room and the perk exist
    def delete(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            room_id = intValidator(request.data['id'])
            room = Room.objects.get(id=room_id)
            if room.hotel.business != request.authorized: #need to check here correctly
                raise Exception

            if len(request.data['amenities']) <= 0:
                raise Exception

            for x in range(0, len(request.data['amenities'])):
                if not(isinstance(request.data['amenities'][x], int)):
                    raise Exception
                amenity = Amenity.objects.get(id=request.data['amenities'][x])
                room.amenities.remove(amenity)
            
            room.updated = timezone.now()
            room.save()
            serializer = RoomSerializer(room)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class RoomImageUploader(APIView):

    def put(self, request):    
        try:
            room_id = request.data['roomId']
            room_priority = request.data['priority']
            room = Room.objects.get(id=room_id)
            if room.hotel.business.id != request.authorized.id:
                raise CustomException("You don't have permission to modify rooms that aren't ours.")

            room_image = RoomImage(photo=request.FILES['photo'], priority=room_priority, room=room)
            room_image.save()
            
            serializer = RoomImageSerializer(room_image)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error  has been occurred.' })

class OneRoomDetails(APIView):

    def post(self, request):
        try:
            room_id = request.data['roomId']
            
            room = Room.objects.get(id=room_id)
            room.views += 1
            room.save()

            serializer = RoomSerializer(room)

            return Response(serializer.data)
        except Exception:
            return Response({ "error": 'An error has been occurred.' })

class MostPopularRooms(APIView):

    def get(self, request):
        try:
            rooms = Room.objects.order_by('-views')[0:4]
            serializer = RoomSerializer(rooms, many=True)

            return Response(serializer.data)
        except Exception:
            return Response({ "error": 'An error has been occurred.' })

class MostRatedRooms(APIView):

    def get(self, request):
        try:
            rooms = Room.objects.order_by('reviews_average')
            serializer = RoomSerializer(rooms)

            return Response(serializer.data)
        except Exception:
            return Response('An error has been occurred.') #STATUS 404?

class PriceRangeRoomSearch(APIView):

    def get(self, request):
        try:
            min_price = request.data['minPrice']#validate
            max_price = request.data['maxPrice']#validate

            rooms = Room.objects.filter(Q(price__gte=min_price) & Q(price__lte=max_price))

            serializer = RoomSerializer(rooms)

            return Response(serializer.data)
        except Exception:
            return Response('An error has been occurred.')

class Test(APIView):

    def get(self, request):
        try:
            rooms = Room.objects.filter(price__gte=100)
            serializer = RoomSerializer(rooms, many=True)

            return Response(serializer.data)
        except Exception as err:
            return Response(str(err))

class MultipliesQueriesRoomSearch(APIView):

    def post(self, request):
        try:
            room = Room.objects

            if request.data['priceRange'] == 'True':
                if request.data['minPrice'] != '-1':
                    min_price = request.data['minPrice']
                    room = room.filter(price__gte=min_price)
                if request.data['maxPrice'] != '-1':
                    max_price = request.data['maxPrice']
                    room = room.filter(price__lte=max_price)

            if request.data['nameSearch'] == 'True':
                name = textValidator(request.data['name'], 40, 2)

                room = room.filter(name__contains=name)

            if request.data['hotelIdSearch'] == 'True':
                hotel_id = request.data['hotelId']
                room = room.filter(hotel_id=hotel_id)

            if request.data['hotelNameSearch'] == 'True':
                hotel_name = request.data['hotelName']
                room = room.filter(hotel__name__contains=hotel_name)

            if request.data['citySearch'] == 'True':
                city = textValidator(request.data['city'], 40, 2)
                room = room.filter(hotel__city__contains=city)
                
            if request.data['stateSearch'] == 'True':
                state = textValidator(request.data['state'], 30, 2)
                room = room.filter(hotel__state__contains=state)
                    
            # if request.data['reviewsSearch'] == 'True':
            #     review_min = request.data['minReview']
            #     review_max = request.data['maxReview']
                
            #     room = room.filter(Q(reviews_average__gte=review_min) & Q(reviews_average__lte=review_max))

            serializer = RoomSerializer(room, many=True)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error has been occurred.' })

