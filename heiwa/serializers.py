from rest_framework.serializers import ModelSerializer

from heiwa.models import order

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