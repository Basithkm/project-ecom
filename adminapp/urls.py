
from django.contrib import admin
from django.urls import path
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/',views.register.as_view(),name='register'),
    path('login/',obtain_auth_token,name='login'),
    path('welcome',views.welcome.as_view(),name='welcome'),
    path('Userdetails/<int:pk>',views.userDetails.as_view(),name='userDetails'),
]