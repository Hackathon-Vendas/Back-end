from rest_framework.serializers import ModelSerializer

from heiwa.models import Order, User, Mesa

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "tittleProduto",
            "description",
            "mesa",
            "status"
        ]

class MesaSerializer(ModelSerializer):
    class Meta:
        model = Mesa
        fields = [
            "id"
        ]

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "password",
            "username"
        ]