from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet

from heiwa.models import Order, User, Mesa
from heiwa.serializers import OrderSerializer, userSerializer, MesaSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer

class MesaViewSet(ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class MPagoViewSet(ViewSet):
    def homepage(self, req):
        return render(req, 'homepage.html')

    def compracerta(self, req):
        return render(req, 'compracerta.html')

    def compraerrada(self, req):
        return render(req, 'compraerrada.html')
