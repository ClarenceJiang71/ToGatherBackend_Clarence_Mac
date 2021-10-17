# from django.shortcuts import render     # Clarence's adjustment starts here
from django.http import HttpResponse

from .models import Event, User_special
from .serializers import EventSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return HttpResponse("API View")


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_special.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]




