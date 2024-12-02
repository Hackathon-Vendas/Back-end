from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from heiwa.models import orders
from heiwa.serializers import ordersSerializer

class ordersViewSet(ModelViewSet):
    queryset = orders.objects.all()
    serializer_class = ordersSerializer
# Create your views here.
