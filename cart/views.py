from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.
def view_cart(request):
    """ View to render the cart content """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Logic to add items shopping cart """
   
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {product.name} to your Cart')

    request.session['cart'] = cart

    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Logic to adjust and update items shopping cart """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    inStock = None
    if 'product.in_stock' in request.POST:
        inStock = request.POST['product.in_stock']
    cart = request.session.get('cart', {})

    if inStock:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            del cart[item_id]
            if not cart[item_id]:
                cart.pop(item_id)
                messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
    else:
        if quantity > 0:
            cart[item_id] = quantity
        else:
            cart.pop(item_id)
            messages.success(request, f'Remove {product.name} from your Cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Logic to remove and update items shopping cart """

    try:
       
       product = get_object_or_404(Product, pk=item_id)
       inStock = None
       if 'product.in_stock' in request.POST:
           inStock = request.POST['product.in_stock']
       cart = request.session.get('cart', {})

       if inStock:
            del cart[item_id] 
            if not cart[item_id]:
               cart.pop(item_id)
               messages.success(request, f'Updated {product.name} quantity to {cart[item_id]}')
       else:
             cart.pop(item_id)
             messages.success(request, f'Remove {product.name} from your Cart')

       request.session['cart'] = cart
       return HttpResponse(status=200)

    except Exception as e:
       messages.error(request, f'Error removing item: {e}')
       return HttpResponse(status=500)
      









