from rest_framework.serializers import ModelSerializer

from heiwa.models import Order, User

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

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "password",
            "username"
        ]