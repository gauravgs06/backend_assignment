from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('listing', views.hotel_listing, name='listing')
]