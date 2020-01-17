"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index_view
from backend.auth_app.urls import urlpatterns as auth_app_urls
from backend.hotel.urls import urlpatterns as hotel_urls
from backend.room.urls import urlpatterns as room_urls
from backend.product.urls import urlpatterns as product_urls
from backend.booking.urls import urlpatterns as booking_urls
# from backend.auth_app import auth_app, hotel, room, product, booking

#I can user routers here to able to only register a few shit here, so this isn't going to be a bloody mess

# urlpatterns = [
#     path('', index_view, name='index'),
#     path('api/admin/', admin.site.urls),
#     path('api/user/', include(auth_app.urls.urlpatterns)),
#     path('api/hotel/', include(hotel.urls.urlpatterns)),
#     path('api/room/', include(room.urls.urlpatterns)),
#     path('api/', include(product.urls.urlpatterns)),
#     path('api/', include(booking.urls.urlpatterns)),
# ]
urlpatterns = [
    path('', index_view, name='index'),
    path('api/admin/', admin.site.urls),
    path('api/user/', include(auth_app_urls)),
    path('api/hotel/', include(hotel_urls)),
    path('api/room/', include(room_urls)),
    path('api/', include(product_urls)),
    path('api/', include(booking_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
