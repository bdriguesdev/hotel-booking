from backend.auth_app.models import Client, Business
from backend.auth_app.serializers import ClientSerializer, BusinessSerializer
import jwt
import json

class CustomAuth:
    def __init__(self, get_response):
        self.get_response = get_response    

    def __call__(self, request):
        # body = json.loads(request.body)
        # request.authorizate = "banana"
        try:
            token = request.headers['Token']
            user_type = request.headers['User-Type']
            #jwt here 
            decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
            user_id = decoded['userId']
            user_email = decoded['userEmail']

            if user_type == 'Client':
                client = Client.objects.get(email=user_email, id=user_id)
                request.authorized = client
            elif user_type == 'Business':
                business = Business.objects.get(email=user_email, id=user_id)
                request.authorized = business
            
            request.user_type = user_type
        except Exception:
            request.authorized = False
            
        response = self.get_response(request)

        return response
