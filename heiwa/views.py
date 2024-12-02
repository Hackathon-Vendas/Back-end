from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from heiwa.models import order
from heiwa.serializers import orderSerializer

class orderViewSet(ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderSerializer
# Create your views here.
