from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from company.models import Company


class CustomUserManager(BaseUserManager):  # 1.

    def create_user(self, email, password=None):  # 2.
        if not email: raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):  # 3.
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    # permissions
    is_owner = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


