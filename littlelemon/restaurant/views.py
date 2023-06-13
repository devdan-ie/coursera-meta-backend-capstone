from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from .models import MenuItem, Booking
from .serializers import MenuItemSerializer, UserSerializer, BookingSerializer


def sayHello(request):
    return HttpResponse('Hello World')


# Create your views here.
def index(request):
    return render(request, 'index.html', {})





# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingsViewSet(viewsets.ModelViewSet):
   queryset = Booking.objects.all()
   serializer_class = BookingSerializer
   permission_classes = [permissions.IsAuthenticated]
