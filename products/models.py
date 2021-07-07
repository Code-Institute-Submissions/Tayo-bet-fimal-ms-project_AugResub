from django.db import models
from django.utils.crypto import get_random_string

# CATEGORY (groceries, 4) - 1
# CATEGORY (groceries2, 5) - 2

# Product (category - groceries) - 1
# Product (category - groceries) - 2

# Create your models here.
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
            

