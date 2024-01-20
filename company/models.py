from django.db import models


class Company(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=90)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"


