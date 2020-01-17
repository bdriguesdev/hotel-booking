from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.db.models import Q
from datetime import datetime

from .models import Booking, Review, DiscountCoupon, RoomPromotion
from backend.hotel.models import Hotel
from backend.room.models import Room
from .serializers import BookingSerializer, ReviewSerializer, BookingCalendarSerializer, ReviewRoomSerializer
from backend.validators import textValidator, numValidator, reviewValueValidator

class CreateBooking(APIView):

    #here I need to do a payment and confirm if it has been sucessful
    #need to check if the room has empty for the days that the client need
    def post(self, request):
        try:
            if request.user_type != 'Client':
                raise Exception

            room_id = request.data['roomId']
            room = Room.objects.get(id=room_id)
            #----NEED TO CHECK IF THE ROOM ISNT EMPTY----#
            #----NEED TO CHECK IF THE ROOM WAS BOOKED ALREADY----#
            date_now = datetime.now()
            start_at = datetime.strptime(request.data['startAt'], "%a, %d %b %Y %H:%M:%S %Z")
            end_at = datetime.strptime(request.data['endAt'], "%a, %d %b %Y %H:%M:%S %Z")
            coupon_name = request.data['coupon']
            if start_at < date_now:
                print('here')
                raise Exception
            if start_at > end_at:
                raise Exception

            bookings = Booking.objects.filter(start__gte=start_at, room_id=room_id)
            if len(bookings) != 0:
                raise Exception

            nights = (end_at - start_at).days
            total_price = nights * room.price
            booking = Booking(client=request.authorized, start=start_at, end=end_at, room=room, total_price=total_price, nights=nights, created=timezone.now())
            booking.save()
            
            if coupon_name != "":
                coupon = DiscountCoupon.objects.get(coupon=coupon_name, expire__gte=date_now)
            
            serializer = BookingSerializer(booking)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('An error has been occurred.')
        #the hotel owner can create a booking of his own hotel to create a day off or should I create a different table for that?

class CancelBooking(APIView):

    #Here I don't actually want to delete the booking but I need to cancel it... so ?
    #Canceled: True ? or create a new table for it? CanceledBookings
    def delete(self, request):
        return Response('Testing')

class getBookingsPerMonth(APIView):

    def post(self, request):
        try:
            room_id = request.data['roomId']
            bookings_month = request.data['bookingsMonth']
            bookings_year = request.data['bookingsYear']

            bookings = Booking.objects.filter(room_id=room_id)
            bookings = bookings.filter(Q(start__year=bookings_year) | Q(end__year=bookings_year))
            bookings = bookings.filter(Q(start__month=bookings_month) | Q(end__month=bookings_month))
            serializer = BookingCalendarSerializer(bookings, many=True)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('An error has been occurred.')

class getBookingsPerMonthWithDetails(APIView):
    
    def post(self, request):
        try:
            if request.authorized == False or request.user_type != 'Business':
                raise Exception("You don't have permission to do this.")

            room_id = request.data['roomId']
            month = request.data['month']
            year = request.data['year']
            room = Room.objects.get(id=room_id)
            if room.hotel.business.id != request.authorized.id:
                raise Exception("You don't have permission to do this.")

            bookings = Booking.objects.filter(room__id=room.id)
            bookings = bookings.filter(Q(start__year=year) | Q(end__year=year))
            bookings = bookings.filter(Q(start__month=month) | Q(end__month=month))

            serializer = BookingSerializer(bookings, many=True)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('An error has been occurred.')

class getHotelBookingsPerMonth(APIView):
    
    def post(self, request):
        try:
            if request.authorized == False or request.user_type == 'Client':
                raise Exception("You don't have permission to acess this.")

            hotel_id = request.data['hotelId']
            month = request.data['month']
            year = request.data['year']
            hotel = Hotel.objects.get(id=hotel_id)
            if hotel.business.id != request.authorized.id:
                raise Exception("You don't have permission to acess this.")

            bookings = Booking.objects.filter(room__hotel=hotel)
            bookings = bookings.filter(Q(start__year=year) | Q(end__year=year))
            bookings = bookings.filter(Q(start__month=month) | Q(end__month=month))

            serializer = BookingCalendarSerializer(bookings, many=True)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('An error has been occurred.')

class getUserBookings(APIView):

    def post(self, request):
       try:
            bookings = Booking.objects

            if request.data['startAtSearch'] == 'True':
                # start_at = ""
                # if request.data['jsUTCString'] == 'True':
                #     start_at = datetime.strptime(request.data['startAt'], "%a, %d %b %Y %H:%M:%S %Z")
                # else:
                start_at = request.data['startAt']
                bookings = bookings.filter(start__gte=start_at)
            if request.data['endAtSearch'] == 'True':
                # end_at = ""
                # if request.data['jsUTCString'] == 'True':
                #     end_at = datetime.strptime(request.data['endAt'], "%a, %d %b %Y %H:%M:%S %Z")
                # else:
                end_at = request.data['endAt']
                bookings = bookings.filter(end__lte=end_at)
            if request.data['citySearch'] == 'True':
                city = request.data['city']
                bookings = bookings.filter(room__hotel__city__contains=city)
            if request.data['stateSearch'] == 'True':
                state = request.data['state']
                bookings = bookings.filter(room__hotel__state__contains=state)
            if request.data['minPriceSearch'] == 'True':
                min_price = request.data['minPrice']
                bookings = bookings.filter(total_price__gte=min_price)
            if request.data['maxPriceSearch'] == 'True':
                max_price = request.data['maxPrice']
                bookings = bookings.filter(total_price__lte=max_price)
            if request.data['reviewSearch'] == 'True':
                review_value = request.data['reviewValue']
                bookings = bookings.filter(review__value=review_value)
            if request.data['clientSearch'] == 'True':
                client_id = request.authorized.id
                bookings = bookings.filter(client_id=client_id)

            serializer = BookingSerializer(bookings, many=True)

            return Response(serializer.data)
       except Exception as err:
           print(err)
           return Response('An error has been occurred.')


class CreateReview(APIView):
    #IMPORTANT:-----------------------------
    #need to check if the user has a finished booking in this room I also need the client id
    #---------------------------------------
    def post(self, request):
        try:
            if request.user_type != 'Client':
                raise Exception

            room_id = request.data['roomId']
            booking_id = request.data['bookingId']
            room = Room.objects.get(id=room_id)
            hotel = Hotel.objects.get(id=room.hotel.id)
            review_description = textValidator(request.data['description'], 250, 0)
            review_value = reviewValueValidator(int(request.data['value']))

            booking = Booking.objects.get(id=booking_id)
            reviews = Review.objects.filter(booking__id=booking_id)
            if len(reviews) != 0:
                raise Exception
            #problem here
            if booking.start > timezone.now():
                raise Exception

            

            #saving review information at the hotel that the room is from
            hotel.reviews_count += 1
            hotel.reviews_total += review_value
            hotel.reviews_average = hotel.reviews_total / hotel.reviews_count
            hotel.save()

            review = Review(value=review_value, booking=booking, description=review_description, room=room, client=request.authorized, created=timezone.now())
            review.save()

            #saving review information at the room
            room.reviews_count += 1
            room.reviews_total += review_value
            room.reviews_average = room.reviews_total / room.reviews_count
            room.reviews.add(review)
            room.save()

            booking.review = review
            booking.save()
            serializer = ReviewSerializer(review)

            return Response(serializer.data)
        except Exception:
            return Response('Send a valid data.')

class getRoomReviews(APIView):

    def post(self, request):
        try:
            room_id = request.data['roomId']
            reviews = Review.objects.filter(room__id=room_id)

            serializer = ReviewRoomSerializer(reviews, many=True)

            return Response(serializer.data)
        except Exception:
            return Response('An error has been occurred.')

class getReviewsAllRoomsFromHotel(APIView):

    def post(self, request):
        try:
            hotel_id = request.data['hotelId']
            reviews = Review.objects.filter(room__hotel__id=hotel_id)

            serializer = ReviewRoomSerializer(reviews, many=True)

            return Response(serializer.data)
        except Exception as err:
            print(err)
            return Response('An error has been occurred.')
class CreatePromotion(APIView):

    def post(self, request):
        try:
            if request.user_type != 'Business':
                raise Exception

            room_id = request.data['roomId']
            min_price = request.data['minPrice']
            max_price = request.data['maxPrice']
            value = request.data['value']
            percentage = request.data['percentage']
            start = request.data['start']
            end = request.data['end']

            room = Room.objects.get(id=room_id)
            if room.hotel.business != request.authorized:
                raise Exception

            room_promotion = RoomPromotion(room=room, min_price=min_price, max_price=max_price, value=value, percentage=percentage, start=start, end=end, created=timezone.now())
            room_promotion.save()

            return Response('Working')
        except Exception:
            return Response('An error has been occurred.')