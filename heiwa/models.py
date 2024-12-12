from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _


class Mesa(models.Model):

     def __str__(self):
        return str(self.id)


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


class UserManager(BaseUserManager):
    """Manager for users."""

    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError("Users must have an email address.")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create, save and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model in the system."""

    passage_id = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("passage_id"),
        help_text=_("Passage ID"),
        default=uuid.uuid4
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name=_("email"),
        help_text=_("Email")
        )
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("name"),
        help_text=_("Username")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Usuário está ativo"),
        help_text=_("Indica que este usuário está ativo.")
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Usuário é da equipe"),
        help_text=_("Indica que este usuário pode acessar o Admin.")
    ),
    username = models.CharField(blank=True, null=True, max_length=255)

    objects = UserManager()
    
    # Mudar email para username
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        """Meta options for the model."""

        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
