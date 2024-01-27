from django.db import models
from company.models import Company


class Restaurant(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=90, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='restaurants')

    def __str__(self):
        return f"{self.name}"
