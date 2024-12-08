from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from heiwa.models import Order, User, Mesa
from heiwa.serializers import OrderSerializer, userSerializer, MesaSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class userViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

class MesaViewSet(ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer
# Create your views here.
