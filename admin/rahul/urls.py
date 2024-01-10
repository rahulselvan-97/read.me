from django.contrib import admin
from django.urls import path
from.import views


urlpatterns = [
    path('home', views.home),
    path('signin',views.signin),
    path('signout',views.signout),
    path('signup',views.signup)
]