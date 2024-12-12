from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet, ViewSet
from heiwa.serializers import OrderSerializer, userSerializer, MesaSerializer
import mercadopago

from heiwa.models import Order, User, Mesa



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

    def redirect(self, req):
        sdk = mercadopago.SDK("TEST-2879295092487193-120819-161acc178b785a39b74a59f20749475f-316571065")

        payment_data = {
            "items": [
                {'id': 1, 'title': 'Produtos', "quantity": 1, "currency_id": "BRL", "unit_price": 250}
            ],
            "back_urls": {
                "success": "http://127.0.0.1:8000/mercadop/compracerta/",
                "failure":"http://127.0.0.1:8000/mercadop/compraerrada/",
                "pending": "http://127.0.0.1:8000/mercadop/compraerrada/",
            },
            
            "auto_return": "all",
        }
        result = sdk.preference().create(payment_data)
        payment = result["response"]
        link_G_pagamento = payment["init_point"]
        
        return JsonResponse({'redirect_url': link_G_pagamento})

            