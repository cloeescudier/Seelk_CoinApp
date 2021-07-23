from app.models import ValueAlert, PercentageAlert, User
from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import ValueAlertSerializer, PercentageAlertSerializer, UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

class ValueAlertViewSet(viewsets.ModelViewSet):
    queryset = ValueAlert.objects.all()
    serializer_class = ValueAlertSerializer
    permission_classes = (IsAuthenticated, )

class PercentageAlertViewSet(viewsets.ModelViewSet):
    queryset = PercentageAlert.objects.all()
    serializer_class = PercentageAlertSerializer
    permission_classes = (IsAuthenticated, )
    
