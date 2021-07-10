from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category

# Create your views here.


def all_products(request):
    """ View for individual product details """

    products = Product.objects.all()
    query = None
    Categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
               sortkey = 'lower_name'
               products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category_id'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            Categories = request.GET['category']
            products = products.filter(category=Categories)
            
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Enter correct search word")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(descriptions__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'store_categories': Category,
        'current_sorting': current_sorting,

    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ All products, sorting and searching  View """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product
    }
    return render(request, 'products/products_detail.html', context)

