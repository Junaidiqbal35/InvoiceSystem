from django.contrib.auth.base_user import BaseUserManager
from django.db import models

# Create your models here.
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class UserManager(BaseUserManager):
    """
    custom model user manager
    """

    def create_user(self, email, password, **extra_fields):
        """
        creates new user with email and password
        :param email:
        :param password:
        :param extra_fields:
        :return: User
        """
        if not email:
            raise ValueError("Please enter your email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        creates and saves super user with given email and password

        :param email:
        :param password:
        :param extra_fields:
        :return:
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("verified", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be a staff member")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("superuser must be an admin")

        user = self.create_user(email, password, **extra_fields)
        return user


class User(AbstractUser):
    """
    custom user model
    """
    username = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True)

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    is_vendee = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Vendee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_vendee")
    bio = models.CharField(max_length=255, default='Vendee')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Vendee'
        verbose_name_plural = 'Vends'


class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_vendor")
    bio = models.CharField(max_length=255, default='Vendor')

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = 'Vendor'
        verbose_name_plural = 'Vendor'


class OrderItems(models.Model):
    vendee = models.ForeignKey(Vendee, on_delete=models.CASCADE)
    item_id = models.PositiveIntegerField()
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name


class DeliveryOrder(models.Model):
    ORDER_STATUS_CHOICES = ((1, "Pending"), (2, "Processing"), (3, "Accepted"), (4, "Rejected"))
    order = models.ForeignKey(OrderItems, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_status = models.PositiveIntegerField(choices=ORDER_STATUS_CHOICES, default=1)

    def __str__(self):
        return self.vendor.user.first_name



