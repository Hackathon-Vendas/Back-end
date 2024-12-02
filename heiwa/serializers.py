from rest_framework.serializers import ModelSerializer

from heiwa.models import order, User

class orderSerializer(ModelSerializer):
    class Meta:
        model = order
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