from django.db import models


class Company(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=40,  verbose_name="Company name")
    address = models.CharField(max_length=90, verbose_name="Company address", blank=True, null=True)
    telephone = models.CharField(max_length=20, verbose_name="Company telephone", blank=True, null=True)
    email = models.EmailField(max_length=254, verbose_name="Company email", blank=True, null=True)

    def __str__(self):
        return f"{self.name}"


