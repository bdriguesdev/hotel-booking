from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
import datetime
import pytz
import jwt

from backend.exceptions import CustomException
from ..validators import passwordValidator, birthdayValidator, emailValidator, stateValidator, cityValidator
from .models import Client, Business
from .serializers import ClientSerializer, BusinessSerializer

class Login(APIView):
    def post(self, request):
        try:
            user_email = emailValidator(request.data['userEmail']) 
            user_password = passwordValidator(request.data['userPassword'])
            user_type = request.data['userType']
            serializer = None
            if user_type == 'Client':
                client = Client.objects.get(email=user_email)
                if not(check_password(user_password, client.password)):
                    raise CustomException('Incorrect email/password.')
                serialiazer = ClientSerializer(client)
                token = jwt.encode({ "userId": client.id, "userEmail":client.email }, 'secret', algorithm='HS256')
            elif user_type == 'Business':
                business = Business.objects.get(email=user_email)
                if not(check_password(user_password, business.password)):
                    raise CustomException('Incorrect email/password.')
                serialiazer = BusinessSerializer(business)
                token = jwt.encode({ "userId": business.id, "userEmail": business.email }, 'secret', algorithm='HS256')
            else:
                raise Exception
            
            return Response({ "token": token, "user": serialiazer.data })
        except CustomException as err:
            return Response({ "error": str(err)})
        except Exception:
            return Response({ "error": 'An error has been occurred.' })

class CreateClient(APIView):
    def post(self, request):
        try:
            first_name = request.data['firstName'].strip()
            last_name = request.data['lastName'].strip()
            birthday = request.data['birthday']
            password = passwordValidator(request.data['password']) 
            state = stateValidator(request.data['state']) 
            city = cityValidator(request.data['city']) #need to validate here
            email = emailValidator(request.data['email'])
            hashed_password =  make_password(password)

            client = Client(first_name=first_name, last_name=last_name, password=hashed_password, state=state, city=city, email=email, birthday=birthday, created=timezone.now(), updated=timezone.now())
            client.save()
            
            serializer = ClientSerializer(client)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error has been occured.' })
        
class CreateBusiness(APIView):
    def post(self, request):
        try:
            name = request.data['name'].strip()
            email = emailValidator(request.data['email'])
            password = passwordValidator(request.data['password'])
            cnpj = 1234567
            city = cityValidator(request.data['city'])
            state = stateValidator(request.data['state'])

            hashedPassword =  make_password(password)

            business = Business(name=name, email=email, password=hashedPassword, cnpj=cnpj, city=city, state=state, created=datetime.datetime.now(), updated=datetime.datetime.now())
            business.save()

            serializer = BusinessSerializer(business)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error has been occurred.' })
        
class UserAvatarUploader(APIView):

    def put(self, request):    
        try:
            user = request.authorized
            if user == False:
                raise CustomException("You don't have permission.")
            
            user.photo = photo=request.FILES['photo']
            user.save()
            
            serializer = None
            if request.user_type == 'Client':
                serializer = ClientSerializer(user)
            elif request.user_type == 'Business':
                serializer = BusinessSerializer(user)

            return Response(serializer.data)
        except CustomException as err:
            return Response({ "error": str(err) })
        except Exception:
            return Response({ "error": 'An error has been occurred.' })