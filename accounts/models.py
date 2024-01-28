from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db import models
from company.models import Company


class User(AbstractUser):

    email = models.EmailField(unique=True, max_length=255)
    company = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    # permissions
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    can_see_company = models.BooleanField(default=False)
    can_see_users = models.BooleanField(default=False)
    can_change_password = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name if self.first_name and self.last_name else self.username


