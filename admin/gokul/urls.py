from django.contrib import admin
from django.urls import path
from.import views
  

urlpatterns=[
    path('bow',views.stunners),
     path('name',views.get_name),
     path('sea',views.article_search_view)
]