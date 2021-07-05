from django.shortcuts import render
from .models import Product

# Create your views here.
def all_products(request):
    """ All products, sorting and searching  View """

    products = Product.objects.all()

    context = {
        'products': products
    }
    return render(request, 'products/products.html', context)
