from datetime import datetime
from django.contrib.auth.models import User
from django_countries.fields import CountryField

from django.db import models
from django.utils.crypto import get_random_string
from django.utils import timezone


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('groceries', 'Groceries'),
        ('soap & lotions', 'Soap & Lotions'),
        ('offers', 'Offers'),
        ('new arrivals', 'New Arrivals'),

    )

    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', to_field='name', null=True, blank=True, on_delete=models.SET_NULL)
    id = models.CharField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageURLs = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name 

    def save(self):
        if not self.id:
            self.id = get_random_string(20)
        super().save()


class ReturnProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    product_id = models.CharField(max_length=20)
    return_reason = models.TextField(max_length=500)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    return_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class ProductFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=254, null=True, blank=True)
    detail = models.TextField(max_length=750)

    def __str__(self):
        return self.name

