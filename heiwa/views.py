from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from heiwa.models import order, User
from heiwa.serializers import orderSerializer, userSerializer

class orderViewSet(ModelViewSet):
    queryset = order.objects.all()
    serializer_class = orderSerializer

class userViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userSerializer
# Create your views here.
