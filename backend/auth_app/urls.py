from django.urls import path

from . import views

urlpatterns = [
    path('test/', views.Test.as_view()),
    path('client/create/', views.CreateClient.as_view()),
    path('login/', views.Login.as_view()),
    path('business/create/', views.CreateBusiness.as_view()),
    path('photo_uploader/', views.UserAvatarUploader.as_view())
]
