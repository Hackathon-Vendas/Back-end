from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from heiwa.models import Order, User
from heiwa.serializers import OrderSerializer, userSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class userViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
# Create your views here.
