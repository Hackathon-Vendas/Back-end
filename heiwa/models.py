from django.db import models

class StatusCompra(models.IntegerChoices):
        A_FAZER = 1, 'A fazer'
        PREPARANDO = 2, 'Preparando'
        PRONTO = 3, 'Pronto'


class orders (models.Model):
    tittleProduto = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    mesa = models.IntegerField(max_length=2)
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.A_FAZER )


      


# Create your models here.
