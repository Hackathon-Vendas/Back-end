from django.db import models
from django.contrib.auth.models import AbstractUser

class StatusCompra(models.IntegerChoices):
        A_FAZER = 1, 'A fazer'
        PREPARANDO = 2, 'Preparando'
        PRONTO = 3, 'Pronto'


class order (models.Model):
    tittleProduto = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    mesa = models.IntegerField()
    status = models.IntegerField(choices=StatusCompra.choices, default=StatusCompra.A_FAZER )


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)

    def __str__(self):
         return self.username


      


# Create your models here.
