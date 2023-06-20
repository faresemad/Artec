from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    STATUS_CHOICES = (
        ("user", "User"),
        ("student_review", "Student Review"),
        ("student_rejected", "Student Rejected"),
        ("student", "Student"),
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="user")
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email
