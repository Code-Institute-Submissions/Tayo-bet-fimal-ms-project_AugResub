from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JCVaeC4ndMENfvqiboA9mWgT97Zao85MdSU9aZuH9wWw4be3FUgJM0rztoYVUROXFROWo0n33xJzfpZkUmkToLp00Nw7D9C9i',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

