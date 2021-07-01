from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.core.validators import MinLengthValidator

# Create your models here.
class Products(models.Model):
    CATEGORY_CHOICES =[
        ('Groceries', 'Groceries'),
        ('Soap&Lotions', 'Soap&Lotions'),
        ('Offers', 'Offers'),
        ('New Arrivals','New Arrivals')
    ]

    categories = models.CharField(max_length=254, null=True, blank=True)
    id = models.CharField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    weight = models.CharField(max_length=254, null=True, blank=True)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinLengthValidator(1)])
    imageURLs = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.pk = get_random_string(10)
        super().save(*args, **args)
