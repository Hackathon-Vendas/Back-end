from django.db import models
from django.contrib.auth.models import AbstractUser

class Mesa(models.Model):
    numeroMesa = models.IntegerField(unique=True)

    def __str__(self):
        return f"Mesa {self.numeroMesa}"


class StatusCompra(models.IntegerChoices):
    A_FAZER = 1, 'A fazer'
    PREPARANDO = 2, 'Preparando'
    PRONTO = 3, 'Pronto'


class Order(models.Model):
    tittleProduto = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    mesa = models.ForeignKey(Mesa, on_delete=models.PROTECT, related_name="pedidos")
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.A_FAZER)

    def __str__(self):
        return f"{self.tittleProduto} - {self.get_status_display()}"


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username
