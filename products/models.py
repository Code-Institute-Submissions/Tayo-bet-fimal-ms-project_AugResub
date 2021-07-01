from django.db import models


# Create your models here.
class category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
    
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Products(models.Model):
    category = models.CharField(max_length=254, null=True, blank=True)
    id = models.CharField(max_length=254, blank=True, primary_key=True)
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    weight = models.CharField(max_length=254, null=True, blank=True)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    imageURLs = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    in_stock = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name   
        