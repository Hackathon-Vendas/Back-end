from rest_framework.serializers import ModelSerializer

from heiwa.models import orders

class ordersSerializer(ModelSerializer):
    class Meta:
        model = orders
        fields = [
            "id",
            "tittleProduto",
            "description",
            "mesa",
            "status"
        ]